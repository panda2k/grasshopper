import reflex as rx
from grasshopper.require_login import require_google_login
from grasshopper.template import template
jsonArray=[{"title":"Intro to Python Workshop","school_name":"UC San Diego","description":"Learn the basics of Python programming in a beginner-friendly environment.","location":"Rady","time":"2024-05-02 18:00:00"},{"title":"Cybersecurity Seminar","school_name":"UC San Diego","description":"Explore the latest trends and challenges in cybersecurity.","location":"Rady","time":"2024-05-10 19:30:00"},{"title":"Data Science Panel","school_name":"UC San Diego","description":"Hear from industry experts about careers in data science.","location":"Rady","time":"2024-05-15 18:30:00"}]
def itinerary(jsonArray):
    #example jsonArray:[{"title":"Intro to Python Workshop","school_name":"UC San Diego","description":"Learn the basics of Python programming in a beginner-friendly environment.","location":"Rady","time":"2024-05-02 18:00:00"},{"title":"Cybersecurity Seminar","school_name":"UC San Diego","description":"Explore the latest trends and challenges in cybersecurity.","location":"Rady","time":"2024-05-10 19:30:00"},{"title":"Data Science Panel","school_name":"UC San Diego","description":"Hear from industry experts about careers in data science.","location":"Rady","time":"2024-05-15 18:30:00"}]
    #make me a div that lists the events, each event as an object as a card displaying time, title, description, location
    return rx.box(
        *[
            rx.box(
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
                                    rx.button(jsonArray[i]["time"], size="1", color_scheme="lime", variant="soft"),
                                    rx.text(jsonArray[i]["title"], size="5", weight="bold"),
                                    flex_direction="column",
                                ),
                                rx.stack(
                                    rx.box(
                                        rx.text("username", size="1"),
                                    ),
                                    rx.box(
                                        rx.icon("bookmark"),
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
                                    rx.text(jsonArray[i]["location"], size="2"),
                                    spacing="2",
                                    align="center",
                                    padding_top="5px",
                                    padding_bottom="5px",
                                ),
                            ),
                            rx.scroll_area(
                                rx.flex(
                                    rx.text(
                                        jsonArray[i]["description"],
                                        size="2",
                                        trim="both",
                                    ),
                                ),
                            ),
                            flex_direction="column",
                            padding="10px",
                        ),
                        padding="10px",
                    ),
                    padding="10px",
                )
                for i in range(len(jsonArray))
            )
        ],
        flex_direction="column",
    )

@template
@require_google_login
def itinerary():
    return rx.center(
        rx.heading("itinerary maker"),
        itinerary(jsonArray),
        align="center",
        spacing="7",
        font_size="2em",
    )
