import json
import time
import datetime 
from dotenv import load_dotenv
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token
import reflex as rx
from reflex.base import os
from sqlmodel import select, or_
from grasshopper.model import AuthenticationSession, Event, School, User, UserBlock, EventData, UserData, SchoolData, EventDataTuple

load_dotenv()

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")

class GlobalState(rx.State): 
    session_id: str = rx.Cookie(name="session_id", max_age=3600)

    @rx.var
    def page_id(self) -> str:
        return self.router.page.params.get("id", "no id")

    @rx.var 
    def event(self) -> Event | None:
        if self.page_id == "no id":
            return None
        with rx.session() as session:
            query = select(Event).where(Event.id == self.page_id)
            return session.exec(query).one()

    def check_in(self): 
        with rx.session() as session:
            block = UserBlock(
                owner_id=self.user.id,
                event_id=self.page_id,
                block_id="1"
            )
            session.add(block)
            session.commit()

    @rx.var
    def checked_in(self) -> bool:
        if self.page_id == "no id" or not self.user:
            return False 

        with rx.session() as session:
            query = select(UserBlock).where(
                UserBlock.owner_id == self.user.id,
                UserBlock.event_id == self.page_id
            )
            return session.exec(query).first() != None


    def create_event(self, form_data: dict):
        """Handle the form submit."""
        with rx.session() as session:
            school_id = self.schools[self.school_names.index(form_data["school"])].id
            event = Event(
                title=form_data["title"],
                description=form_data["description"],
                location=form_data["location"],
                time=datetime.datetime.strptime(form_data["time"], "%Y-%m-%dT%H:%M"),
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
    def schools(self) -> list[School]:
        with rx.session() as session:
            query = select(School)
            return list(session.exec(query).all())

    @rx.var 
    def school_names(self) -> list[str]:
        names = []
        for s in self.schools:
            names.append(s.name)
        return names

    @rx.var
    def user_created_events(self) -> list[EventDataTuple]:
        if not self.user:
            return []

        with rx.session() as session:
            query = select(Event, User, School).join(User).join(School).where(Event.author_id == self.user.id)
            results = session.exec(query).all()
            events = []
            for event, user, school in results:
                # events.append(event)
                event_data = EventData(
                    description=event.description,
                    event_id=event.id,
                    location=event.location,
                    school_id=event.school_id,
                    title=event.title,
                    time=event.time.strftime("%b %d, %Y @ %-I %p"),
                    author_id=event.author_id
                )
                user_data = UserData(
                    user_name=user.name,
                    image=user.image,
                    user_id=user.id,
                    email=user.email
                )
                school_data = SchoolData(
                    school_name=school.name,
                    school_id=school.id
                )
                events.append((json.loads(event_data.toJSON()), json.loads(user_data.toJSON()), json.loads(school_data.toJSON())))
            return events

    @rx.var
    def user_attended_events(self) -> list[EventDataTuple]:
        if not self.user:
            return []
        with rx.session() as session:
            block_events = []
            for block in self.user_blocks:
                block_events.append(block.event_id)
            query = select(Event, User, School).join(User).join(School).where(
                or_(*map(lambda id: Event.id == id, block_events))
            )
            results = session.exec(query).all()
            events = []
            for event, user, school in results:
                event_data = EventData(
                    description=event.description,
                    event_id=event.id,
                    location=event.location,
                    school_id=event.school_id,
                    title=event.title,
                    time=event.time.strftime("%b %d, %Y @ %-I %p"),
                    author_id=event.author_id
                )
                user_data = UserData(
                    user_name=user.name,
                    image=user.image,
                    user_id=user.id,
                    email=user.email
                )
                school_data = SchoolData(
                    school_name=school.name,
                    school_id=school.id
                )
                events.append((json.loads(event_data.toJSON()), json.loads(user_data.toJSON()), json.loads(school_data.toJSON())))
            return events

    @rx.var
    def user_blocks(self) -> list[UserBlock]:
        if not self.user:
            return []
        with rx.session() as session:
            query = select(UserBlock).where(UserBlock.owner_id == self.user.id)
            return list(session.exec(query))

    @rx.var 
    def count_user_blocks(self) -> int:
        return len(self.user_blocks)

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

    is_attending: bool = False

    def toggle_text(self):
        """An event handler to toggle between "Attend" and "Attending"."""
        # Event handlers can modify the base var.
        # Here we reference the base var `is_attending`.
        self.is_attending = not self.is_attending

    @rx.var
    def button_text(self) -> str:
        """A computed var that returns the current button text."""
        # Computed var returns "Attend" if is_attending is False, otherwise returns "Attending".
        return "Attending" if self.is_attending else "Attend"
    
    def is_authenticated(self) -> bool:
        return bool(self.auth_session)

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

