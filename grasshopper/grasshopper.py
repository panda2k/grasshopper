"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import os

from reflex.event import redirect
from rxconfig import config

import reflex as rx

from grasshopper.pages.index import index
from grasshopper.pages.profile import profile

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

########## DYNAMIC ROUTES #############    
class State(rx.State):
    """The app state."""
    @rx.var
    def user_id(self) -> str:
        return self.router.page.params.get("userID", "no userID")    

@rx.page(route="/post/[userID]")
def user():
    """A page that updates based on the route."""
    return rx.heading(State.user_id)

app = rx.App()
app.add_page(index, route="/",title="My Beautiful App")
app.add_page(profile, route="/profile",title="Profile")

