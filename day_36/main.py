from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv(".venv/.env")
account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_KEY")
my_number = os.getenv("MY_NUMBER")
client = Client(account_sid, auth_token)

msg = "MSG HERE :)"

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=msg,
  to='whatsapp:' + my_number
)

print(message.sid)