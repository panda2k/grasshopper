from dotenv import load_dotenv
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token
import reflex as rx
from reflex.base import os
from sqlmodel import select
from grasshopper.model import AuthenticationSession, User

load_dotenv()

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")

class GlobalState(rx.State): 
    auth_session: None | AuthenticationSession = None

    def on_success(self, id_token: dict):
        auth_response = verify_oauth2_token(
            id_token["credential"],
            requests.Request(),
            GOOGLE_CLIENT_ID,
        )

        if not self.auth_session:
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
                    session.expire_on_commit = False
                    new_auth_session = AuthenticationSession(user_id=user.id)
                    session.add(new_auth_session)
                    session.commit()
                    return new_auth_session

                query = select(User).where(User.email == auth_response["email"])
                results = session.exec(query).first()
                user = results if results else create_user()

                self.auth_session = create_session()

