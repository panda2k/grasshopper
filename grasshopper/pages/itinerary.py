import reflex as rx
from grasshopper.require_login import require_google_login
from grasshopper.template import template
jsonArray=[{"title":"Intro to Python Workshop","school_name":"UC San Diego","description":"Learn the basics of Python programming in a beginner-friendly environment.","location":"Rady","time":"2024-05-02 18:00:00"},{"title":"Cybersecurity Seminar","school_name":"UC San Diego","description":"Explore the latest trends and challenges in cybersecurity.","location":"Rady","time":"2024-05-10 19:30:00"},{"title":"Data Science Panel","school_name":"UC San Diego","description":"Hear from industry experts about careers in data science.","location":"Rady","time":"2024-05-15 18:30:00"}]
def itinerary(jsonArray):
    #example jsonArray:[{"title":"Intro to Python Workshop","school_name":"UC San Diego","description":"Learn the basics of Python programming in a beginner-friendly environment.","location":"Rady","time":"2024-05-02 18:00:00"},{"title":"Cybersecurity Seminar","school_name":"UC San Diego","description":"Explore the latest trends and challenges in cybersecurity.","location":"Rady","time":"2024-05-10 19:30:00"},{"title":"Data Science Panel","school_name":"UC San Diego","description":"Hear from industry experts about careers in data science.","location":"Rady","time":"2024-05-15 18:30:00"}]
    #make me a div that lists the events, each event as an object as a card displaying time, title, description, location
    cardList = []
    for i in range(len(jsonArray)):
        rx.box(
            rx.box(
                rx.box(
                        rx.box(
                            rx.stack(
                                rx.stack(
                                    rx.text(jsonArray[i]["time"], size="1", color_scheme="lime", variant="soft"),
                                    rx.text(jsonArray[i]["title"], size="5", weight="bold"),
                                    flex_direction="column",
                                ),
                                flex_direction="row",
                                justify="between",
                                width="100%",
                            ),
                            rx.flex(
                                rx.icon("map-pin", size=15),
                                rx.text(jsonArray[i]["location"], size="2"),
                                spacing="2",
                                align="center",
                                padding_top="5px",
                                padding_bottom="5px",
                            ),
                            rx.text(
                                jsonArray[i]["description"],
                                size="2",
                                trim="both",
                            ),
                        ),
                        padding="10px",
                )
                
            )
    )
    return 

        

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
