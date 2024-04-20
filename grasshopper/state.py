import time 
from dotenv import load_dotenv
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token
import reflex as rx
from reflex.base import os
from sqlmodel import select
from grasshopper.model import AuthenticationSession, Event, User

load_dotenv()

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")

class GlobalState(rx.State): 
    session_id: str = rx.Cookie(name="session_id", max_age=3600)

    def create_event(self, form_data: dict):
        """Handle the form submit."""
        schools: Dict[str, str] = {
            "UCSD": "1234",
            "UCI": "5678"
        }
        with rx.session() as session:
            school_id = schools[form_data["school"]]
            event = Event(
                title=form_data["title"],
                description=form_data["description"],
                school_id=school_id, 
                author_id=self.user.id
            )
            session.add(event)
            session.commit()

    @rx.var
    def token_is_valid(self) -> bool:
        try:
            return bool(
                self.token_info
                and int(self.token_info.get("exp", 0))
                > time.time()
            )
        except Exception:
            return False

    @rx.cached_var
    def user(self) -> User | None:
        with rx.session() as session:
            if not self.token_is_valid:
                return None
            query = select(User).where(User.id == self.authentication_session.user_id)
            return session.exec(query).one()

    @rx.var
    def authentication_session(self) -> AuthenticationSession | None:
        with rx.session() as session:
            session.expire_on_commit = False
            query = select(AuthenticationSession).where(AuthenticationSession.id == self.session_id)
            results = session.exec(query).first()
            return results
     
    @rx.cached_var
    def token_info(self) -> dict[str, str]:
        try:
            if not self.authentication_session:
                raise Exception("No authentication session")

            return verify_oauth2_token(
                self.authentication_session.credential,
                requests.Request(),
                GOOGLE_CLIENT_ID,
                clock_skew_in_seconds=10
            )
        except Exception as exc:
            print(f"Error verifying token: {exc}")
        return {}

    def on_success(self, id_token: dict):
        auth_response = verify_oauth2_token(
            id_token["credential"],
            requests.Request(),
            GOOGLE_CLIENT_ID,
            clock_skew_in_seconds=10
        )
        with rx.session() as session:
            def create_user(): 
                user = User(
                    email=auth_response["email"],
                    name=auth_response["name"],
                    image=auth_response["picture"]
                ) 
                session.add(user)
                session.commit()
                return user
            
            def create_session():
                new_auth_session = AuthenticationSession(
                    user_id=user.id,
                    credential=id_token["credential"]
                )
                session.add(new_auth_session)
                session.commit()
                return new_auth_session

            session.expire_on_commit = False
            query = select(User).where(User.email == auth_response["email"])
            results = session.exec(query).first()
            user = results if results else create_user()

            auth_session = create_session()
            self.session_id = auth_session.id

