import json
from typing import Tuple
import reflex as rx
import uuid
from sqlmodel import Field
from datetime import datetime, timezone
from dataclasses import dataclass

def create_id():
    return str(uuid.uuid4())

class Event(rx.Model, table=True):
    id: str = Field(
        default_factory=create_id,
        primary_key=True,
        nullable=False,
    )
    title: str
    description: str
    image: str | None = Field(default=None)
    location: str
    time: datetime = Field()
    school_id: str = Field(foreign_key="school.id")
    author_id: str = Field(foreign_key="user.id")

class School(rx.Model, table=True):
    id: str = Field(
        default_factory=create_id,
        primary_key=True,
        nullable=False,
    )
    name: str

class User(rx.Model, table=True):
    id: str = Field(
        default_factory=create_id,
        primary_key=True,
        nullable=False,
    )
    email: str
    name: str
    image: str | None = Field(default=None)

class Block(rx.Model, table=True):
    id: str = Field(
        default_factory=create_id,
        primary_key=True,
        nullable=False,
    )
    image: str 
    title: str

class UserBlock(rx.Model, table=True):
    id: str = Field(
        default_factory=create_id,
        primary_key=True,
        nullable=False,
    )
    block_id: str = Field(foreign_key="block.id")
    owner_id: str = Field(foreign_key="user.id")
    event_id: str = Field(foreign_key="event.id")
    acquired_date: datetime = Field(default=datetime.now(timezone.utc))

class AuthenticationSession(rx.Model, table=True):
    id: str = Field(
        default_factory=create_id,
        primary_key=True,
        nullable=False,
    )
    credential: str 
    user_id: str = Field(foreign_key="user.id")

@dataclass
class EventData:
    description: str
    event_id: str
    location: str
    # image:str
    school_id: int
    title: str
    time: str
    author_id: str

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)


@dataclass
class UserData:
    user_name: str
    image: str
    user_id: str
    email: str

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)


@dataclass
class SchoolData:
    school_name: str
    school_id: str

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

EventDataTuple = Tuple[dict, dict, dict]
