# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 23:27:02 2020

@author: Ayush
"""
import smtplib
from datetime import datetime
from email.message import EmailMessage

t1 = datetime.now()

DEFAULT_DATA_PATH = r'PATH'
smtp_config = {}
filepath = DEFAULT_DATA_PATH + "/smtpconfig.txt"

with open(filepath) as mail_file:
    for line in mail_file:
        name, var = line.partition("=")[::2]
        smtp_config[name.strip()] = var.strip()
        

s = smtplib.SMTP_SSL(host=smtp_config["smtpserver_host"], port=smtp_config["smtpserver_port"])
s.login(smtp_config["username"], smtp_config["password"])

t2 = datetime.now()

message = EmailMessage()

message.set_content("email_message")
message['Subject'] = "Restaurant Bot | List of {0} Restaurants in {1}"


message['From'] = smtp_config["from_email"]
message['To'] = "MAIL_ADDRESS"
   
s.send_message(message)
s.quit()
print(t2-t1)