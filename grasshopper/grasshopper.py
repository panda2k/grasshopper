"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

class State(rx.State):
    """The app state."""
    @rx.var
    def user_id(self) -> str:
        return self.router.page.params.get("userID", "no userID")

@rx.page(route="/", title="My Beautiful App")
def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text("Get started by editing ", rx.code(filename)),
            rx.button(
                "Check out our docs!",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            rx.logo(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )

@rx.page(route="/scan", title="Scan QR")
def scan():
    return rx.center(
        rx.heading("Scan QR code", size="9"),
        rx.text("Scan the QR code to get started"),
        rx.button(
            "Scan",
            on_click=lambda: rx.redirect("/profile"),
            size="4",
        ),
        align="center",
        spacing="7",
        font_size="2em",
    )
    
@rx.page(route="/profile", title="INSERT USER")
def profile():
    return rx.center(
        rx.heading("Profile", size="9"),
        rx.text("Please enter your name"),
        rx.input(placeholder="Name"),
        rx.button(
            "Submit",
            on_click=lambda: rx.redirect("/itinerary"),
            size="4",
        ),
        align="center",
        spacing="7",
        font_size="2em",
    )

@rx.page(route="/itinerary", title="Your DAY itinerary")
def itinerary():
    return rx.center(
        rx.heading("Itinerary", size="9"),
        rx.text("This is your itinerary for the day"),
        rx.button(
            "Home",
            on_click=lambda: rx.redirect("/"),
            size="4",
        ),
        align="center",
        spacing="7",
        font_size="2em",
    )
    

########## DYNAMIC ROUTES #############    
@rx.page(route="/post/[userID]")
def user():
    """A page that updates based on the route."""
    return rx.heading(State.user_id)


app = rx.App()
