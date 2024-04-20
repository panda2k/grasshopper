import reflex as rx
from grasshopper.template import template

@template
def profile():
    return rx.flex(
        rx.image(src="/profilepic.png", width="3em", padding="15px"),
        rx.vstack(
            rx.box(
                rx.text("username", size="6"),
            ),
            rx.box(
                rx.text("5 friends • 3 events", size="2")
            ),
        ),
        rx.divider(),
        rx.container(
            rx.center(  # idk how to vertically center
                rx.image(src="/profile-blocks.png", width="5em")
            ),
            background="#f1f1f1",
            width="100%",
            height="300px",
        ),
        rx.divider(),
        rx.container(
            rx.center(
                rx.text("saved", size="4"),
                rx.text("attended", size="4"),
                rx.text("host", size="4"),
                align="center",
                spacing="7",
                padding="15px"
            ),
            rx.box(
                rx.text("add cards similar to home screen", size="3")
            ),
        ),
        align="center",
        spacing="2",
        flex_wrap="wrap",
        font_size="2em",
    )