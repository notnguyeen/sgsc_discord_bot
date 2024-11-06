# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file


class Config:
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    PREFIX = "!"  # Define your command prefix here
