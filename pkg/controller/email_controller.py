from fastapi import APIRouter, HTTPException
from pkg.dto.email_dto import EmailDTO
from pkg.service.email_service import EmailService

router = APIRouter(tags=["email"], responses={
    400: {"description": "Bad Request"},
    500: {"description": "Internal Server Error"},
})

email_service = EmailService()

@router.post("/api/internal/emails/send/v1")
async def send_email(request: EmailDTO):
    try:
        result = email_service.process_request(request)

        if result.get("success") is not True or result is None:
            raise HTTPException(
                status_code=400,
                detail=result.get("message", "Errore durante invio email"),
            )
        return result

    except HTTPException as e:
        raise e

    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
