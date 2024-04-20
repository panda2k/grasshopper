##### LAYOUT #####

from typing import Callable

import reflex as rx

def navbar() -> rx.Component:
    #create a footer with 5 elements, that link to 5 pages
    #style it so that it is in the bottom of the page 
    return rx.box(
        rx.flex(
            rx.link(rx.icon("home"), href="/"),
            rx.link(rx.icon("calendar-clock"), href="/itinerary"),
            rx.link(rx.icon("scan-eye"), href="/scan"),
            # rx.link("Contact", href="/contact"),
            rx.link(rx.icon("circle-user"), href="/profile"),
            spacing="3",
            justify="center",
            align="center",
            justify_content="space-evenly",
        ),
        padding="1em",
        background_color="black",
        color="white",
        position="fixed",  
        bottom="0",
        left="0",
        width="100%", 

    )


def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.box(
        page(),
        navbar(),
        padding_bottom="4em",
    )