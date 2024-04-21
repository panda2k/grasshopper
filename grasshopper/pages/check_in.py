import reflex as rx
from grasshopper.require_login import require_google_login
from grasshopper.state import GlobalState

@rx.page(route="/event/[id]/check-in")
@require_google_login
def check_in():
    """A page that updates based on the route."""
    return rx.cond(
        GlobalState.page_id == "no id",
        rx.heading("Event not found"), 
            rx.vstack(
                rx.box(
                    rx.box(
                        rx.link(rx.icon("circle-chevron-left",size=24), href="/",color="black",style={"position":'absolute',"top":'10px',"left":'10px',"background-color":'white',"border-radius":'50%','padding':'5px','z-index':'1'}),
                        rx.box(
                            rx.image(
                                src="/blocks-stack.jpg",
                                style={
                                    "width": "30%",
                                    "object-fit": "cover",
                                    "object-position": "center",
                                    "border-radius": "10px",
                                    "margin-bottom": "10px",
                                },
                            ),
                            width="100%",
                            style={"background-color": "#F1F1F1", "justify-content": "center"},
                            display="flex",
                        ),
                        rx.box(
                            rx.heading(GlobalState.event[0]["title"], as_="h1",trim="normal",size="5"),
                            rx.text(GlobalState.event[1]["user_name"], weight="medium", trim="normal",size="4"),
                            rx.text(GlobalState.event[2]["school_name"], weight="light", trim="normal",size="3",style={"margin-bottom":'15px', "margin-top":'10px'}),
                            rx.box(
                                rx.flex(
                                    rx.box(
                                        rx.flex(
                                            rx.icon("clock-3"),
                                            rx.text(GlobalState.event[0]["time"], size="2"),
                                            spacing="2",align="center")
                                    ),
                                    rx.box(
                                        rx.flex(
                                            rx.icon("map-pin"),
                                            rx.text(GlobalState.event[0]["location"], size="2"),
                                            spacing="2",align="center"
                                        ),
                                        style={"margin-top": "8px"}
                                    ),
                                    spacing="0",
                                    style={"border-radius":'10px', "border":'1px solid #e0e0e0',"padding":'15px', "align-items":'start', "flex-direction": "column"},
                                    align="center",
                                ),
                                style={"border-radius":'10px',},
                            ),
                            rx.flex(
                                rx.text(
                                    GlobalState.event[0]["description"],
                                    size="2",
                                    trim="both",
                                ),
                                type="always",
                                scrollbars="vertical",
                                style={"padding-top": "1.5em"},
                            ),
                            as_child=True,
                            width="100vw",
                            style={"padding":'20px',"background-color":'white'},
                        ),
                    ), 
                    width="100%"
                ), 
                rx.box(
                    rx.button(
                        rx.cond(
                            GlobalState.checked_in,
                            rx.flex(
                                rx.text("Checked In", size="5"),
                                rx.icon("circle-check"),
                                align="center",
                                spacing='3'
                            ),
                            rx.flex(
                                rx.text("Check In", size="5"),
                                rx.icon("arrow-up-right"),
                                align="center",
                                spacing='3'
                            ),
                        ),
                        style={"background-color":'black',"color":'white','width':'60vw',"border-radius":'50px',"padding":'30px',"position":'fixed',"bottom":'70px',"left":'50%',"transform":'translateX(-50%)'},
                        on_click=GlobalState.check_in
                    ),
                    style={"width": "100%"}
                )
            )
    )

app = rx.App()
