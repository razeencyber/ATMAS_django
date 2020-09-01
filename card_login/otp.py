# OTP system for ATMAS
# run pip install twilio on terminal
from decouple import config
import math
import random
import twilio
from twilio.rest import Client

string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = len(string)


def send_otp(card_number, phone_number):

    otp = ""
    for i in range(6):
        otp += string[math.floor(random.random() * length)]

    auth_sid = config('twilio_sid')
    auth_token = config('twilio_token')
    client = Client(auth_sid, auth_token)

    message = client.messages.create(body="Your 6 digit OTP is: " + otp,
                                     from_='+12564190069',
                                     to=f'+91{phone_number}')

    return message.sid, otp
