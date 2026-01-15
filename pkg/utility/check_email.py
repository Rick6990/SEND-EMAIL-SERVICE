from pkg.dto.utente_dto import UtenteDTO


def email_reserve(utente: UtenteDTO) -> tuple[str, str]:
    subject = "Conferma Prenotazione"
    body = (
        f"Ciao {utente.nome},\n"
        f"Hai prenotato '{utente.titoloLibro}' in data {utente.data.strftime('%d/%m/%Y')}.\n"
        f"Ti avviseremo quando il libro sarà disponibile."
    )
    return subject, body


def email_return(utente: UtenteDTO) -> tuple[str, str]:
    subject = "Restituzione Avvenuta"
    body = (
        f"Ciao {utente.nome},\n"
        f"Hai restituito '{utente.titoloLibro}' in data {utente.data.strftime('%d/%m/%Y')}.\n"
        f"Grazie per aver utilizzato il nostro servizio!"
    )
    return subject, body
