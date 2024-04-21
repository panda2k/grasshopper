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
                        #create me a static save button at the top right of the page, i want it overlayed over my image, give it white background circle
                        rx.link(
                            rx.icon("bookmark-x",size=24), 
                            href="/",
                            color="black",
                            style={"position":'absolute',"top":'10px',"right":'10px',"background-color":'white',"border-radius":'50%','padding':'5px','z-index':'1'}
                        ),
                        rx.image(
                            src="https://acmucsd.s3.us-west-1.amazonaws.com/portal/events/46f1a42e-41e5-4103-8052-74d3e13d6a62.png",                
                            style={
                                "height": "30vh","width": "100%","object-fit": "cover","object-position": "center",
                            },
                        ),
                        rx.box(
                            rx.heading("ACM Kickoff", as_="h1",trim="normal",size="5"),
                            rx.text("ACM @ UCSD", weight="medium", trim="normal",size="4"),
                            rx.text("UC San Diego • 4/27", weight="light", trim="normal",size="3",style={"margin-bottom":'15px', "margin-top":'10px'}),
                            rx.box(
                                rx.flex(
                                    rx.box(
                                        rx.flex(
                                            rx.icon("clock-3"),
                                            rx.text("5:00 PM", size="2"),
                                            spacing="2",align="center")
                                    ),
                                    rx.box(rx.text("|", size="4",weight="light")),
                                    rx.box(
                                        rx.flex(
                                            rx.icon("map-pin"),
                                            rx.text("Price Center West Ballroom", size="2"),
                                            spacing="2",align="center")
                                    ),
                                    spacing="0",
                                    style={"border-radius":'10px', "border":'1px solid #e0e0e0',"padding":'15px', "justify-content":'space-evenly'},
                                    align="center",
                                ),
                                style={"border-radius":'10px',},
                            ),
                            as_child=True,
                            width="100vw",
                            style={"padding":'20px',"background-color":'white'},
                        )
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
