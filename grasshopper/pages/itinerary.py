import reflex as rx
from grasshopper.require_login import require_google_login
from grasshopper.template import template

def action_bar() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.input(
            placeholder="Ask a question",
            width="300px"
            # on_change=State.set_question,
            # style=style.input_style,
        ),
            rx.button(
                "Ask",
                on_click=ItineraryState.click_button
                # on_click=State.answer,
                # style=style.button_style,
            ),
        ),
        padding="10px",
        position="fixed",
        bottom="50px",
        justify="center",
        width="100vw",
    )

def itineraryJSON(jsonObj: dict):    #example jsonObj"title":"Intro to Python Workshop","school_name":"UC San Diego","description":"Learn the basics of Python programming in a beginner-friendly environment.","location":"Rady","time":"2024-05-02 18:00:00"},{"title":"Cybersecurity Seminar","school_name":"UC San Diego","description":"Explore the latest trends and challenges in cybersecurity.","location":"Rady","time":"2024-05-10 19:30:00"},{"title":"Data Science Panel","school_name":"UC San Diego","description":"Hear from industry experts about careers in data science.","location":"Rady","time":"2024-05-15 18:30:00"}]
    #make me a div that lists the events, each event as an object as a card displaying time, title, description, location
        return rx.box(
                rx.box(
                    rx.stack(
                        rx.stack(
                            rx.text(jsonObj["time"], size="1", color_scheme="lime", variant="soft"),
                            rx.text(jsonObj["title"], size="5", weight="bold"),
                            flex_direction="column",
                        ),
                        flex_direction="row",
                        justify="between",
                        width="100%",
                    ),
                    rx.flex(
                        rx.icon("map-pin", size=15),
                        rx.text(jsonObj["location"], size="2"),
                        spacing="2",
                        align="center",
                        padding_top="5px",
                        padding_bottom="5px",
                    ),
                    rx.text(
                        jsonObj["description"],
                        size="2",
                        trim="both",
                    ),
                ),
                padding="10px",
        )


def jsonArrayContainer(rxObj):
    return rx.box(rxObj)

jsonArray: list[dict]=[
    {
        "title":"Intro to Python Workshop",
        "school_name":"UC San Diego",
        "description":"Learn the basics of Python programming in a beginner-friendly environment.",
        "location":"Rady",
        "time":"May 2, 2024 @ 6:00PM"
    },
    {
        "title":"Cybersecurity Seminar",
        "school_name":"UC San Diego",
        "description":"Explore the latest trends and challenges in cybersecurity.",
        "location":"Rady",
        "time":"May 10, 2024 @ 7:30PM"
    },
    {
        "title":"Data Science Panel",
         "school_name":"UC San Diego",
         "description":"Hear from industry experts about careers in data science.",
         "location":"Rady",
         "time":"May 15, 2024 @ 8:00AM"
    }
]

class ItineraryState(rx.State):
    button_clicked: bool = False 

    def click_button(self):
        self.button_clicked = True

@template
@require_google_login
def itinerary():
    return rx.stack(
        rx.heading("itinerary maker"),
        action_bar(),
        rx.cond(
            ItineraryState.button_clicked,
            rx.vstack(*map(lambda i: itineraryJSON(i), jsonArray)),
            rx.box()
        ),
        align="center",
        flex_direction="column",
        spacing="7",
        font_size="2em",
    )
