##### LAYOUT #####

from typing import Callable

import reflex as rx




def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.box(
        page(),
        rx.logo(),
        padding_bottom="4em",
    )