from twilio.rest import Client
import os
from dotenv import load_dotenv

# extract your api credentials from a .env file using the load_dotenv() function. You can also set them as environment variables and use os.environ() method instead.

def send_message(number, amount, item):
    
    account_sid = 'YOUR_SID'
    auth_token = 'YOUR_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:YOUR_TWILIO_PHONE_NUMBER',
    body=f'Thank you for shopping with us! \nYour purchased item: \n{item}.\n\nTotal amount paid: Rs. {amount}/-',
    to=f'whatsapp:+91{number}'
    )
