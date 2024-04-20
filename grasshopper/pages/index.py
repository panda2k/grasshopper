"""The main index page."""

import reflex as rx
from grasshopper.template import template

from grasshopper.template import template

# def eventCard(imageSrc, title, description, author, school):
def eventCard():
    return rx.box(
        rx.box(
            rx.image(src="https://acmucsd.s3.us-west-1.amazonaws.com/portal/events/46f1a42e-41e5-4103-8052-74d3e13d6a62.png",
                style={
                    "height": "70%","width": "100%","object-fit": "cover","object-position": "center","border-radius": "10px","margin-bottom": "10px",
                },
            ),
            rx.flex(
                rx.box(
                    rx.stack(
                        rx.stack(
                            rx.button("today @ 7pm", size="1", color_scheme="lime", variant="soft"),
                            rx.text("ACM Kickoff", size="5", weight="bold"),
                            flex_direction="column"
                        ),
                        rx.stack(
                            rx.box(
                                rx.image(src="/profilepic-trimmed.jpeg", width="15px"),
                            ),
                            rx.box(
                                rx.text("username", size="1"),
                            ),
                            flex_direction="row",
                            justify="end",
                        ),
                        flex_direction="row",
                        justify="between",
                        width="100%",
                    ),
                    rx.box(
                        rx.flex(
                            rx.icon("map-pin", size=15),
                            rx.text("Price Center West Ballroom", size="2"),
                            spacing="2",
                            align="center",
                            padding_top="5px",
                            padding_bottom="5px",
                        ),
                    ),
                    rx.scroll_area(
                        rx.flex(
                            rx.text(
                                "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                size="2",
                                trim="both",
                            ),
                            type="always",
                            scrollbars="vertical",
                            style={"height": 55},
                        ),
                    ),
                    spacing="1",
                    height="100%",
                ),
                padding_left="10px",
                padding_right="10px",
            ),
            as_child=True,
        ),
        style={"width":"100%", "margin":"10px"},
    )

@template
# @require_google_login
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("EVENTS"),
            rx.stack(
                rx.select(
                    items=GlobalState.school_names,
                    placeholder="school",
                    name="school",
                    required=True,
                ),
                rx.input(
                    placeholder="search here...",
                    width="200px",
                ),
                flex_direction="row",
                justify="center",
                width="100%",
            ),
            eventCard(),
            rx.divider(),
            eventCard(),
            rx.divider(),
            eventCard(),
            rx.divider(),
            eventCard(),
            rx.divider(),
            rx.text("no more events to show (╯︵╰,)", weight="light", trim="normal",size="2",style={"margin-bottom":'1em'},color_scheme="lime"),
            align="center",
            spacing="2",
            font_size="2em",
        ),
        padding_bottom="1em"
    )
