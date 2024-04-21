from datetime import datetime
import reflex as rx
from grasshopper.state import GlobalState

def create_event():
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.button(rx.icon("circle-plus"), color_scheme="lime"),
        ),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.box(
                        rx.icon("chevron-down", width="8em"),
                    ),
                    rx.vstack(
                        rx.box(
                            rx.image(src="/blocks-stack.png", width="8em"),
                            padding_top="3em",
                        ),
                        rx.box(
                            rx.heading("create event", align="center"),
                            padding="1em"
                        ),
                        align="center",
                        justify="center",
                        width="100%"
                    ),
                    rx.form(
                        rx.vstack(
                            rx.box(
                                rx.input(
                                    placeholder="title",
                                    name="title",
                                    required=True,
                                    width="250px",
                                ),
                                width="100%",
                            ),
                            rx.text_area(
                                placeholder="description",
                                name="description",
                                required=True,
                                width="250px",
                            ),
                            rx.select(
                                items=GlobalState.school_names,
                                placeholder="school",
                                name="school",
                                required=True,
                                width="250px",
                            ),
                            rx.input(
                                placeholder="location",
                                name="location",
                                required=True,
                                width="250px",
                            ),
                            # add a note here to make them set the date and time in PST
                            rx.input(
                                type="datetime-local",
                                name="time",
                                min=f"{datetime.now().strftime('%Y-%m-%dT%h:%M')}",
                                width="250px",
                            ),
                            rx.button("create!", type="submit", variant="soft"),
                            align="center",
                            gap="2em",
                            width="100%",
                        ),
                        on_submit=GlobalState.create_event,
                        reset_on_submit=True,
                        align="center",
                        justify="center",
                    ),
                    width="100%",
                    align="center",
                ),
                height="90%",
                padding="2em",
                background_color="#FFF",
            ),
        ),
        direction="bottom"
    )
