import os
import logging


class Settings:
    FILE_LOCATION = os.path.join(os.path.expanduser("~"), "ebayklein.db")
    LOGGING = os.environ.get("LOGGING") or logging.ERROR
    URL_BASE = "https://www.kleinanzeigen.de"
    NTFY_URL = "SERVER URL HERE"
    NTFY_TOKEN = "tk_xxxxxxxxxxxxxxxxx"


settings = Settings()
