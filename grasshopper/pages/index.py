"""The main index page."""

import reflex as rx

@template
def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.button(
                "Check out our docs!",
                size="4",
            ),
            rx.logo(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )