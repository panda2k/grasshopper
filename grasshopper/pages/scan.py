import reflex as rx
from grasshopper.template import template


@template
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
