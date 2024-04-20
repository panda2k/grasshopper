import reflex as rx

@template
def profile():
    return rx.center(
        rx.heading("Profile", size="9"),
        rx.text("Please enter your name"),
        rx.input(placeholder="Name"),
        align="center",
        spacing="7",
        font_size="2em",
    )