import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pkg.config.mailtrap_config import ConnectionSMTP
#from pkg.dto.email_dto import EmailDTO
#from pkg.utility.check_email import email_reserve, email_return

class EmailService:
    
    def __init__(self):
        self.smtp_server = ConnectionSMTP.SMTP_SERVER_NAME
        self.smtp_port = ConnectionSMTP.SMTP_PORT
        self.smtp_user = ConnectionSMTP.SMTP_USER
        self.smtp_password = ConnectionSMTP.SMTP_PASSWORD
        self.sender_email = ConnectionSMTP.SMTP_SENDER_EMAIL

        if not all([self.smtp_server, self.smtp_port, self.smtp_user, self.smtp_password,self.sender_email]):
            raise ValueError("Configurazione SMTP incompleta!")


    def send_email(self, recipient_email: str, subject: str, body: str) -> dict:
        try:
            message = MIMEMultipart()
            message["Subject"] = subject
            message["From"] = self.sender_email
            message["To"] = recipient_email
            message.attach(MIMEText(body, 'plain'))
            

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.sender_email, recipient_email, message.as_string())
            
            return {f'Email inviata a {recipient_email}',}
        
        except smtplib.SMTPAuthenticationError as e:
            return {
                'success': False,
                'message': 'Autenticazione SMTP fallita',
                'error': str(e)
            }
        except Exception as e:
            return {
                'success': False,
                'message': 'Errore durante invio email',
                'error': str(e)
            }
