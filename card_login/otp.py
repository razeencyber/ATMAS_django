# OTP system for ATMAS
# run pip install twilio on terminal
from decouple import config
from datetime import datetime
import math
import random
import twilio
from twilio.rest import Client

string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = len(string)

auth_sid = config('twilio_sid')
auth_token = config('twilio_token')
client = Client(auth_sid, auth_token)


def send_otp(card_number, phone_number):

    otp = ""
    for i in range(6):
        otp += string[math.floor(random.random() * length)]

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %d/%m/%y")
    message = client.messages.create(
        body=
        f"Your 6 digit OTP is: {otp} for card number {card_number} at {current_time}",
        from_='+12564190069',
        to=f'+91{phone_number}')
    return message.sid, otp


def send_warn(card_number, phone_number):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %d/%m/%y")
    message = client.messages.create(
        body=
        f"Some one tried to access your card with number {card_number} on {current_time}",
        from_='+12564190069',
        to=f'+91{phone_number}')
    return message.sid
