import reflex as rx

class Event(rx.Model, table=True):
    title: str
    school_id: str
    author_id: str

class User(rx.Model, table=True):
    email: str
    profile_pic: str

