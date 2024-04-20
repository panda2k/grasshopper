import reflex as rx
import uuid
from sqlmodel import Field
from datetime import datetime, timezone

class Event(rx.Model, table=True):
    id: str = Field(
        default=uuid.uuid4,
        primary_key=True,
        nullable=False,
    )
    title: str
    description: str
    image: str | None = Field(default=None)
    school_id: int = Field(foreign_key="school.id")
    author_id: int = Field(foreign_key="user.id")

class School(rx.Model, table=True):
    id: str = Field(
        default=uuid.uuid4,
        primary_key=True,
        nullable=False,
    )
    name: str

class User(rx.Model, table=True):
    id: str = Field(
        default=uuid.uuid4,
        primary_key=True,
        nullable=False,
    )
    email: str
    image: str | None = Field(default=None)

class Block(rx.Model, table=True):
    id: str = Field(
        default=uuid.uuid4,
        primary_key=True,
        nullable=False,
    )
    image: str 
    title: str

class UserBlock(rx.Model, table=True):
    id: str = Field(
        default=uuid.uuid4,
        primary_key=True,
        nullable=False,
    )
    block_id: int = Field(foreign_key="block.id")
    owner_id: int = Field(foreign_key="user.id")
    event_id: int = Field(foreign_key="event.id")
    acquired_date: datetime = Field(default=datetime.now(timezone.utc))

class AuthenticationSession(rx.Model, table=True):
    id: str = Field(
        default=uuid.uuid4,
        primary_key=True,
        nullable=False,
    )
    user_id: str = Field(foreign_key="user.id")
    refresh_token: str

