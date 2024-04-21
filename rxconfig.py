import reflex as rx
from dotenv import load_dotenv
import os

load_dotenv()

#TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
#TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

db_url=f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_URL}:5432/postgres"

config = rx.Config(
    app_name="grasshopper",
    db_url=f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_URL}:5432/postgres"
    #db_url=f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true",
)
