import reflex as rx
from grasshopper.template import template
from grasshopper.model import User, UserBlock
from typing import List, Tuple
from dataclasses import dataclass
from sqlmodel import select
import json

@dataclass
class UserData:
    user_name: str
    image: str
    user_id: str
    email:str

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

@dataclass
class UserBlockData:
    block_id: str
    owner_id: str
    id: str

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

UserBlockTuple = Tuple[dict, dict]

class LeaderboardState(rx.State):
    @rx.var
    def rankings(self) -> List[UserBlockTuple]:
        with rx.session() as session:
            query = select(User, UserBlock).join(UserBlock)
            result = session.exec(query).all()
            results = []
            for user, block in result:
                user_data = UserData(
                    user_name=user.name,
                    image=user.image,
                    user_id=user.id,
                    email=user.email
                )
                block_data = UserBlockData(
                    block_id = block.block_id,
                    owner_id=block.owner_id,
                    id=block.id,
                )
                results.append((json.loads(user_data.toJSON()), json.loads(block_data.toJSON())))
            return results

def leaderboard_component(userBlock: UserBlockTuple):
    return rx.center(
        rx.box(
            rx.image(src="/profilepic.png", width="3em"),
            width="15%",
        ),
        rx.box(
            rx.text(userBlock[0]["user_name"]),
            width="63%",
        ),
        rx.box(
            rx.image(src="/grass-block.png", width="2em"),
            width="10%",
        ),
        rx.spacer(),
        rx.box(
            rx.text("2"),
            width="10%",
        ),
        width="100%",
        justify="center",
    )

@template
def private_leaderboard():

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
            rx.foreach(LeaderboardState.rankings, leaderboard_component),
            width="100%",
            padding_bottom="1em",
        ),
        rx.link(rx.button("global →", align="center", variant="soft"), href="/global-leaderboard"),
        align="center",
        justify="center",
        direction="column",
    )
