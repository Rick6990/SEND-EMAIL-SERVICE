from fastapi import FastAPI
from pkg.controller.email_controller import router as email_router

app = FastAPI(
    title="Send Email Service",
    description="Servizio di invio email",
    version="1.0.0"
)

app.include_router(email_router)

