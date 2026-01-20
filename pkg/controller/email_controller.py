from fastapi import APIRouter, HTTPException
from pkg.dto.email_dto import EmailDTO

import boto3
import json


router = APIRouter(tags=["email"], responses={
    400: {"description": "Bad Request"},
    500: {"description": "Internal Server Error"},
})




#@router.post("/api/internal/emails/send/v1")
async def send_email(request: EmailDTO):
    try:
        sqs = boto3.client(
            'sqs',
            endpoint_url='http://localhost:4566',
            region_name='us-east-1',
            aws_access_key_id='test',
            aws_secret_access_key='test'
        )
        queue_url = 'http://localhost:4566/000000000000/email-queue'

        message_body = {
            "email": request.email,
            "subject": request.subject,
            "body": request.body
        }

        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message_body)
        )

        return {"success": True, "message": "Email inviata in coda SQS", "sqs_message_id": response.get("MessageId")}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
