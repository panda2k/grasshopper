import os
import reflex as rx

from grasshopper.react_google_auth import GoogleLogin, GoogleOAuthProvider
from grasshopper.state import GlobalState

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")

def login() -> rx.Component:
    return GoogleOAuthProvider.create(
        GoogleLogin.create(on_success=GlobalState.on_success),
        client_id=GOOGLE_CLIENT_ID,
    )
