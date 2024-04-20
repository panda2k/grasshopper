import reflex as rx

@template
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
