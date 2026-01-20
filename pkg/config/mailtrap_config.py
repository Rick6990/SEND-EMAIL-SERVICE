import os
from dotenv import load_dotenv

load_dotenv(override=True) # override= true: Serve per sovrascrivere i valori all'interno di .env

class ConnectionSMTP:
    SMTP_SERVER_NAME = os.getenv("SMTP_SERVER_NAME")
    SMTP_PORT = int(os.getenv("SMTP_PORT"))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    SMTP_SENDER_EMAIL = os.getenv("SMTP_SENDER_EMAIL")
