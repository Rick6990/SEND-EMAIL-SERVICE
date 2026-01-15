from enum import Enum
from pydantic import BaseModel, EmailStr
from pkg.dto.utente_dto import UtenteDTO

class OperationType(str, Enum):
    RESERVE = "RESERVE"
    RETURN = "RETURN"

class EmailDTO(BaseModel):
    emailType: str
    utente: UtenteDTO
    recipient_email: EmailStr
