from datetime import date
from pydantic import BaseModel

class UtenteDTO(BaseModel):
    nome: str
    titoloLibro: str
    data: date
