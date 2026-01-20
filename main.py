from threading import Thread
from fastapi import FastAPI
from pkg.controller.email_controller import router as email_router
from pkg.service.listener import MailListener

listen = MailListener()


app = FastAPI(
    title="Send Email Service",
    description="Servizio di invio email",
    version="1.0.0"
)
app.include_router(email_router)

listener_thred = Thread(target=listen.listen(), daemon=True)
listener_thred.start()