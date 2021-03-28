"""
    WhatsApp Auto Messenger
    - Send message to your friend or group at scheduled time

    Author      : Sudhanshu Motewar
    Date  : 25/03/21
"""

import pywhatkit
import re

print("Enter number in format of +91********** or **********")

# take inputs from user
receiver = input("Enter mobile no. of Receiver = ")
message = input("Enter message = ")
hour, minute = input("Enter time to send message - 24 hrs format (hh:mm) = ").strip().split(":")

# pattern to check valid phone no.
pattern = '^(\+[9][1])?[0-9]{10}$'
result = re.match(pattern, receiver)

if result:
    # pattern to check if number start with +91
    pattern = '^\+[9][1]'
    if not re.match(pattern, receiver):
        # if phone number do not start with +91 then add it at beginning
        receiver = '+91' + receiver
    # send the message using sendwhatmsg() function
    pywhatkit.sendwhatmsg(receiver, message, int(hour), int(minute))

# To send message to whatsapp group use below function
# pywhatkit.sendwhatmsg_to_group(GroupID, message, time_hour, time_min, wait_time)

# Tip : Only Admin can get GroupID using invite link
