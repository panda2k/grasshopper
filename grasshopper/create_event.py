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
                    rx.flex(
                        rx.heading("Create Event"),
                        rx.drawer.close(
                            rx.button(rx.icon("circle-x"), color_scheme="lime"),
                        ),
                        justify="between",
                        width="100%"
                    ),
                    rx.form(
                        rx.vstack(
                            rx.input(
                                placeholder="Title",
                                name="title",
                                required=True
                            ),
                            rx.input(
                                placeholder="Description",
                                name="description",
                                required=True
                            ),
                            rx.select(
                                placeholder="School",
                                name="school",
                                required=True,
                                items=["UCSD", "UCI"],
                            ),
                            rx.button("Create", type="submit"),
                        ),
                        on_submit=GlobalState.create_event,
                        reset_on_submit=True,
                    ),
                    width="100%"
                ),
                height="90%",
                padding="2em",
                background_color="#FFF"
            ),
        ),
        direction="bottom"
    )
