"""The main index page."""

import reflex as rx
from grasshopper.template import template

from grasshopper.react_google_auth import GoogleLogin, GoogleOAuthProvider
from grasshopper.state import GlobalState
from grasshopper.template import template
import os
from dotenv import load_dotenv

# def eventCard(imageSrc, title, description, author, school):
def eventCard():
    return rx.box(
                (rx.box(
                rx.image(src="https://acmucsd.s3.us-west-1.amazonaws.com/portal/events/46f1a42e-41e5-4103-8052-74d3e13d6a62.png",                
                style={
                    "height": "70%","width": "100%","object-fit": "cover","object-position": "center","border-radius": "10px","margin-bottom": "14px",
                },
),
                rx.flex(
                    rx.box(
                        rx.heading("ACM Kickoff", as_="h1",trim="normal",size="5"),
                        rx.text("ACM @ UCSD", weight="medium", trim="normal",size="4"),
                        rx.text("UC San Diego", weight="light", trim="normal",size="3",style={"margin-bottom":'10px'}),
                        rx.scroll_area(
                            rx.flex(
                                rx.text(
                                    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                    size="2",
                                    trim="both",
                                ),
                                type="always",
                                scrollbars="vertical",
                                style={"height": 55, },
                        ),
                    ),
                    spacing="1",
                    height="100%",
                    style={"margin-bottom":"10px"}
                ),
            ),
            as_child=True,
        ))
    # , border_radius="10px",
    # style={"width":"100%", "padding":"14px", "margin":"10px", "box-shadow":"0 4px 8px 0 rgba(0,0,0,0.2)"})
    ,
    style={"width":"100%", "padding":"14px", "margin":"10px", "border-bottom":"1px solid #e0e0e0"},)



load_dotenv()

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")


@template
# @require_google_login
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Events", size="6"),
            eventCard(),
            eventCard(),
            eventCard(),
            eventCard(),
            rx.text("This is the end of your events", weight="light", trim="normal",size="3",style={"margin-bottom":'10px'}),
            align="center",
            spacing="2",
            font_size="2em",
        ),
        padding="1em",
        # height="100vh",
    )
