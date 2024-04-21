from typing import Callable

import reflex as rx

from grasshopper.create_event import create_event
from grasshopper.state import GlobalState

def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.link(rx.icon("home"), href="/",color="white"),
            rx.cond(
                GlobalState.token_is_valid,
                rx.link(rx.icon("calendar-clock"), href="/itinerary",color="white"),
                rx.button(rx.icon("calendar-clock"), color="white", disabled=True),
            ),
            rx.cond(
                GlobalState.token_is_valid,
                create_event(),
                rx.button(rx.icon("circle-plus"), color="white", disabled=True),
            ),
            rx.link(rx.icon("bar-chart"), href="/private-leaderboard", color="white"),
            rx.link(rx.icon("circle-user"), href="/profile",color="white"),
            spacing="3",
            justify="center",
            align="center",
            justify_content="space-evenly",
        ),
        padding="10px",
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
        padding="2em",
    )
