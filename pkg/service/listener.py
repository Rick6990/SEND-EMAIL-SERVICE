from pkg.service.email_service import EmailService
import boto3
import json

class MailListener:
    
    def listen(self):
        self.sqs = boto3.client('sqs', endpoint_url='http://localhost:4566',
                        region_name='us-east-1',
                        aws_access_key_id='test', aws_secret_access_key='test')

        queue_url = 'http://localhost:4566/000000000000/email-queue'
        email_service = EmailService()

        while True:
            self.response = self.sqs.receive_message(QueueUrl=queue_url, WaitTimeSeconds=10)

            if 'Messages' in self.response:
                for msg in self.response['Messages']:
                    try:
                        body = json.loads(msg['Body'])
                        if isinstance(body, dict) and 'Message' in body:
                            email_data = json.loads(body['Message'])
                        else:
                            email_data = body
                    except Exception as e:
                        print(f"Errore parsing messaggio: {e}")
                        self.sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg['ReceiptHandle'])
                        continue

                    print(f"\n📧 Email ricevuta:")
                    print(f"   A: {email_data['email']}")
                    print(f"   Oggetto: {email_data['subject']}")
                    print(f"   Testo: {email_data['body']}")
                    
                    result = email_service.send_email(
                        recipient_email=email_data['email'],
                        subject=email_data['subject'],
                        body=email_data['body']
                    )
                    print(f"{result}")

                    self.sqs.delete_message(QueueUrl=queue_url, 
                                    ReceiptHandle=msg['ReceiptHandle'])
                    print("Elaborata\n")
