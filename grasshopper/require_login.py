import functools
import reflex as rx
import os
from dotenv import load_dotenv
from grasshopper.login import login
from grasshopper.react_google_auth import GoogleOAuthProvider

from grasshopper.state import GlobalState

load_dotenv()

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")

def require_google_login(page) -> rx.Component:
    @functools.wraps(page)
    def _auth_wrapper() -> rx.Component:
        return GoogleOAuthProvider.create(
            rx.cond(
                GlobalState.is_hydrated,
                rx.cond(
                    GlobalState.token_is_valid, page(), login()
                ),
                rx.heading("Loading...")
            ),
            client_id=GOOGLE_CLIENT_ID,
        )

    return _auth_wrapper
