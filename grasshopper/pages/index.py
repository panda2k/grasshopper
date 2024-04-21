"""The main index page."""

from typing import List
import reflex as rx
from sqlmodel import select
from grasshopper.state import GlobalState
from grasshopper.template import template
from grasshopper.model import Event, User, School, EventData, UserData, SchoolData, EventDataTuple
import json

def event_card(event: EventDataTuple):
    return rx.vstack(
        rx.box(
            rx.box(
                rx.image(
                    src="https://acmucsd.s3.us-west-1.amazonaws.com/portal/events/46f1a42e-41e5-4103-8052-74d3e13d6a62.png",
                    style={
                        "height": "70%","width": "100%","object-fit": "cover","object-position": "center","border-radius": "10px","margin-bottom": "10px",
                    },
                ),
                rx.flex(
                    rx.box(
                        rx.stack(
                            rx.stack(
                                rx.button(event[0]["time"], size="1", color_scheme="lime", variant="soft"),
                            ),
                            rx.stack(
                                rx.box(
                                    rx.image(src="/profilepic-trimmed.jpeg", width="15px"),
                                ),
                                rx.box(
                                    rx.text(event[1]["user_name"], size="1"),
                                ),
                                rx.box(rx.icon("bookmark")),
                                flex_direction="row",
                                justify="end",
                            ),
                            flex_direction="row",
                            justify="between",
                            width="100%",
                        ),
                        rx.text(event[0]["title"], size="5", weight="bold"),
                        rx.box(
                            rx.flex(
                                rx.icon("map-pin", size=15),
                                rx.text(event[0]["location"], size="2"),
                                spacing="2",
                                align="center",
                                padding_top="5px",
                                padding_bottom="5px",
                            ),
                        ),
                        rx.scroll_area(
                            rx.flex(
                                rx.text(
                                    event[0]["description"],
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
                        width="100%"
                    ),
                    padding_left="10px",
                    padding_right="10px",
                ),
                as_child=True,
            ),
            style={"width":"100%"},
        ),
        rx.divider()
    )

class HomeState(rx.State):
    @rx.cached_var
    def events(self) -> List[EventDataTuple]:
        with rx.session() as session:
            query = select(Event, User, School).join(User).join(School)
            results = session.exec(query).all()
            events = []
            for event, user, school in results:
                event_data = EventData(
                    description=event.description,
                    event_id=event.id,
                    location=event.location,
                    school_id=event.school_id,
                    title=event.title,
                    time=event.time.strftime("%b %d, %Y @ %-I %p"),
                    author_id=event.author_id
                )
                user_data = UserData(
                    user_name=user.name,
                    image=user.image,
                    user_id=user.id,
                    email=user.email
                )
                school_data = SchoolData(
                    school_name=school.name,
                    school_id=school.id
                )
                events.append((json.loads(event_data.toJSON()), json.loads(user_data.toJSON()), json.loads(school_data.toJSON())))
            return events

    school_name: str = "UC San Diego"
    def change_school_name(self, name: str):
        self.school_name = name

    search_query: str = ""
    def change_search(self, query: str):
        self.search_query = query

    @rx.var
    def filtered_events(self) -> List[EventDataTuple]:
        filtered = []
        for event, user, school in self.events:
            if school["school_name"] != self.school_name:
                continue
            if self.search_query and self.search_query.lower() not in event["title"].lower():
                continue

            filtered.append((event, user, school))

        return filtered

@template
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
                    default_value=GlobalState.school_names[0],
                    on_change=HomeState.change_school_name
                ),
                rx.input(
                    placeholder="search here...",
                    width="200px",
                    on_change=HomeState.change_search
                ),
                flex_direction="row",
                justify="center",
                width="100%",
            ),
            rx.foreach(
                HomeState.filtered_events,
                event_card
            ),
            rx.text("no more events to show (╯︵╰,)", weight="light", trim="normal",size="2",style={"margin-bottom":'1em'},color_scheme="lime"),
            align="center",
            spacing="2",
            font_size="2em",
        ),
        padding_bottom="1em"
    )
