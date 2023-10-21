import requests
import random
from rest_framework.response import Response
from django.conf import settings
from twilio.rest import Client

account_sid = settings.ACCOUNT_SID
auth_token = settings.AUTH_TOKEN
client = Client(account_sid, auth_token)

def send_otp(phone_number):
    
    otp = random.randint(1000,9999)
    
    to_number = "+91"+phone_number  # Replace with the recipient's actual number
    print("phone number is",to_number,phone_number)

# Define the message you want to send
    
    message = client.messages.create(
    body=f'Dear Customer,Your OTP is: {otp}',
    from_='+17695536270',  # Get your Twilio phone number from the Twilio Console
    to=to_number
    )
    print("messages sid is",message.sid)
    if message.sid:
        return otp
    else:
        raise ConnectionError("Error get")

# Print the message SID to confirm that the message was sent
    # print(f'Message SID: {message.sid}')


# Your Twilio Account SID and Auth Token


# Create a Twilio client

# Generate a random 6-digit OTP

# The recipient's mobile number (include the country code)



    # api_key = settings.API_KEY
    # url = f'https://2factor.in/API/V1/{api_key}/SMS/{phone_number}/{otp}'
    # try:
    #         response = requests.get(url)
    # except ConnectionError:
    #     return Response("You are not connected to internet!!! 🕸")
        
