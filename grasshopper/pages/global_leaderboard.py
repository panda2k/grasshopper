import reflex as rx
from grasshopper.template import template

@template
def global_leaderboard():
    return rx.center(
        rx.image(src="/plant.gif", width="7em", padding_bottom="1em"),
        rx.vstack(
            rx.center(
                rx.box(
                    rx.heading("private leaderboard", align="center"),
                    width="100%",
                ),
                width="100%",
                align="center",
                justify="center",
                padding_bottom="1em",
            ),
            rx.center(
                rx.box(
                    rx.image(src="/profilepic.png", width="3em"),
                    width="15%",
                ),
                rx.box(
                    rx.text("username"),
                    width="63%",
                ),
                rx.box(
                    rx.image(src="/grass-block.png", width="2em"),
                    width="10%",
                ),
                rx.spacer(),
                rx.box(
                    rx.text("55"),
                    width="10%",
                ),
                width="100%",
                justify="center",
            ),
            rx.center(
                rx.box(
                    rx.image(src="/profilepic.png", width="3em"),
                    width="15%",
                ),
                rx.box(
                    rx.text("username"),
                    width="63%",
                ),
                rx.box(
                    rx.image(src="/grass-block.png", width="2em"),
                    width="10%",
                ),
                rx.spacer(),
                rx.box(
                    rx.text("53"),
                    width="10%",
                ),
                width="100%",
                justify="center",
            ),
            rx.center(
                rx.box(
                    rx.image(src="/profilepic.png", width="3em"),
                    width="15%",
                ),
                rx.box(
                    rx.text("username"),
                    width="63%",
                ),
                rx.box(
                    rx.image(src="/grass-block.png", width="2em"),
                    width="10%",
                ),
                rx.spacer(),
                rx.box(
                    rx.text("52"),
                    width="10%",
                ),
                width="100%",
                justify="center",
            ),
            rx.center(
                rx.box(
                    rx.image(src="/profilepic.png", width="3em"),
                    width="15%",
                ),
                rx.box(
                    rx.text("username"),
                    width="63%",
                ),
                rx.box(
                    rx.image(src="/grass-block.png", width="2em"),
                    width="10%",
                ),
                rx.spacer(),
                rx.box(
                    rx.text("50"),
                    width="10%",
                ),
                width="100%",
                justify="center",
            ),
            rx.center(
                rx.box(
                    rx.image(src="/profilepic.png", width="3em"),
                    width="15%",
                ),
                rx.box(
                    rx.text("username"),
                    width="63%",
                ),
                rx.box(
                    rx.image(src="/grass-block.png", width="2em"),
                    width="10%",
                ),
                rx.spacer(),
                rx.box(
                    rx.text("45"),
                    width="10%",
                ),
                width="100%",
                justify="center",
            ),
            rx.center(
                rx.box(
                    rx.image(src="/profilepic.png", width="3em"),
                    width="15%",
                ),
                rx.box(
                    rx.text("username"),
                    width="63%",
                ),
                rx.box(
                    rx.image(src="/grass-block.png", width="2em"),
                    width="10%",
                ),
                rx.spacer(),
                rx.box(
                    rx.text("42"),
                    width="10%",
                ),
                width="100%",
                justify="center",
            ),
            rx.center(
                rx.box(
                    rx.image(src="/profilepic.png", width="3em"),
                    width="15%",
                ),
                rx.box(
                    rx.text("username"),
                    width="63%",
                ),
                rx.box(
                    rx.image(src="/grass-block.png", width="2em"),
                    width="10%",
                ),
                rx.spacer(),
                rx.box(
                    rx.text("39"),
                    width="10%",
                ),
                width="100%",
                justify="center",
            ),
            rx.center(
                rx.box(
                    rx.image(src="/profilepic.png", width="3em"),
                    width="15%",
                ),
                rx.box(
                    rx.text("username"),
                    width="63%",
                ),
                rx.box(
                    rx.image(src="/grass-block.png", width="2em"),
                    width="10%",
                ),
                rx.spacer(),
                rx.box(
                    rx.text("39"),
                    width="10%",
                ),
                width="100%",
                justify="center",
            ),
            rx.center(
                rx.box(
                    rx.image(src="/profilepic.png", width="3em"),
                    width="15%",
                ),
                rx.box(
                    rx.text("username"),
                    width="63%",
                ),
                rx.box(
                    rx.image(src="/grass-block.png", width="2em"),
                    width="10%",
                ),
                rx.spacer(),
                rx.box(
                    rx.text("35"),
                    width="10%",
                ),
                width="100%",
                justify="center",
            ),
            rx.center(
                rx.box(
                    rx.image(src="/profilepic.png", width="3em"),
                    width="15%",
                ),
                rx.box(
                    rx.text("username"),
                    width="63%",
                ),
                rx.box(
                    rx.image(src="/grass-block.png", width="2em"),
                    width="10%",
                ),
                rx.spacer(),
                rx.box(
                    rx.text("33"),
                    width="10%",
                ),
                width="100%",
                justify="center",
            ),
            width="100%",
            padding_bottom="1em",
        ),
        rx.link(rx.button("← private", align="center", variant="soft"), href="/private-leaderboard"),
        align="center",
        justify="center",
        direction="column",
    )