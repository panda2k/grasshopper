##### LAYOUT #####

from typing import Callable
import os.path

import reflex as rx

from grasshopper.create_event import create_event
from grasshopper.state import GlobalState

def navbar() -> rx.Component:
    #create a footer with 5 elements, that link to 5 pages
    #style it so that it is in the bottom of the page 
    return rx.box(
        rx.flex(
            rx.link(rx.icon("home"), href="/",color="white"),
            rx.link(rx.icon("calendar-clock"), href="/itinerary",color="white"),
            rx.cond(
                GlobalState.token_is_valid,
                create_event(),
                rx.flex()
            ),
            rx.link(rx.icon("circle-user"), href="/profile",color="white"),
            spacing="3",
            justify="center",
            align="center",
            justify_content="space-evenly",
        ),
        padding="1em",
        background_color="#121212",
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
        padding="1em",
    )
