import reflex as rx
from grasshopper.pages.index import event_card
from grasshopper.template import template
from grasshopper.require_login import require_google_login
from grasshopper.state import GlobalState

@template
@require_google_login
def profile():
    return rx.flex(
        rx.image(src="/profilepic.png", width="3em", padding="15px"),
        rx.vstack(
            rx.box(
                rx.text(GlobalState.user.name, size="6"),
            ),
            rx.box(
                rx.text(f"5 friends • {GlobalState.count_user_blocks} events", size="2")
            ),
        ),
        rx.divider(),
        rx.container(
            rx.center(
                rx.center(
                    rx.image(src="/profile-blocks.png", width="5em")
                ),
                background="#f1f1f1",
                width="100%",
                height="300px",
            ),
            align="center",
            justify="center"
        ),
        rx.divider(),
        rx.center(
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("saved", value="saved"),
                    rx.tabs.trigger("attended", value="attended"),
                    rx.tabs.trigger("hosted", value="hosted"),
                    size="2",
                ),
                rx.tabs.content(
                    rx.text("item on tab 1"),
                    value="saved",
                ),
                rx.tabs.content(
                    rx.box(
                        rx.foreach(
                            GlobalState.user_attended_events,
                            event_card
                        ),
                    ),
                    value="attended",
                ),
                rx.tabs.content(
                    rx.box(
                        rx.foreach(
                            GlobalState.user_created_events,
                            event_card
                        ),
                    ),
                    value="hosted",
                ),
                default_value="attended"
            ),
            width="100%"
        ),
        align="center",
        spacing="2",
        flex_wrap="wrap",
        font_size="2em",
    )
