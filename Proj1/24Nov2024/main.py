import os

from dotenv import load_dotenv

import imaplib
import email
load_dotenv()

userName = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

def connect_to_mail():
    mail=imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(userName,password)
    mail.select("inbox")
    return mail
