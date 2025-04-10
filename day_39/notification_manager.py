import os
from twilio.rest import Client
from dotenv import load_dotenv

class NotificationManager:
    
    def __init__(self):
        load_dotenv("./.venv/.env")
        self.account_sid = os.getenv("TWILIO_ACC_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_KEY")
        self.my_number = os.getenv("MY_NUMBER")
        self.client = Client(self.account_sid, self.auth_token)
        

    def send_msg(self, msg):
        message = self.client.messages.create(
            from_='whatsapp:+14155238886',
            body=msg,
            to=f'whatsapp:{self.my_number}'
        )
        if message.status:
            print("Sent!")
        else:
            print(message.error_code)
            print(message.error_message)