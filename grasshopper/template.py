##### LAYOUT #####

from typing import Callable

import reflex as rx

from dashboard.navigation import dashboard_sidebar
from dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY


def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.box(
        page(),
        rx.logo(),
        dashboard_sidebar,
        background_color=BACKGROUND_COLOR,
        font_family=FONT_FAMILY,
        padding_bottom="4em",
    )