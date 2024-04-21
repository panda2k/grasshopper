import reflex as rx
from grasshopper.require_login import require_google_login
from grasshopper.template import template

@template
@require_google_login
def itinerary():
    return rx.center(
        rx.heading("itinerary maker"),
        align="center",
        spacing="7",
        font_size="2em",
    )
