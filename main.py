from twilio.rest import Client
import os
from dotenv import load_dotenv

def send_message(number, amount, item):
    
    #load_dotenv()
    account_sid = 'AC151e0515d07100e64726d6dff5ef286f'
    auth_token = '9a3d7206573c3ad4cf5b730ac3c8a6d1'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f'Thank you for shopping with us! \nYour purchased item: \n{item}.\n\nTotal amount paid: Rs. {amount}/-',
    to=f'whatsapp:+91{number}'
    )