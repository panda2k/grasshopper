"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import os

from reflex.event import redirect
from grasshopper import login
from grasshopper.react_google_auth import GoogleOAuthProvider
from grasshopper.state import GlobalState
from rxconfig import config

import reflex as rx

from grasshopper.pages.index import index
from grasshopper.pages.profile import profile
from grasshopper.pages.uniquePage import uniquePage
from grasshopper.pages.attend import attend


docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

import functools

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")


########## DYNAMIC ROUTES #############
class State(rx.State):
    """The app state."""
    @rx.var
    def user_id(self) -> str:
        return self.router.page.params.get("userID", "no userID")


# @rx.page(route="/post/[userID]")
# def user():
#     """A page that updates based on the route."""
#     return rx.heading(GlobalState.user_id)

app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="lime",
        radius="small"
    )
)
app.add_page(index, route="/",title="Grasshopper")
app.add_page(profile, route="/profile",title="Profile")
app.add_page(uniquePage, route="/uniquePage",title="Profile")
app.add_page(attend, route="/attend",title="Profile")
# app.add_page(create, route="/create",title="Create Event")
app.add_page(profile, route="/leaderboard",title="Leaderboard")

