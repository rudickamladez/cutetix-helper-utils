"""Module for easy sending emails"""
# Import smtplib for the actual sending function.
from redmail import EmailSender

# Here are the email package modules we'll need.
from email.message import EmailMessage

# Import os for getting values of ENV vars
import os
import sys

# HTTP lib
import requests

API_URL = os.getenv("API_URL")
EVENT_ID = os.getenv("EVENT_ID")
SMTP_TO = os.getenv("SMTP_TO")


def get_default_message():
    msg = EmailMessage()
    msg['From'] = os.getenv('SMTP_FROM')
    return msg


def get_default_sender():
    return os.getenv('SMTP_FROM')


def get_mail_client():
    """Return predefined client"""
    return EmailSender(
        host=os.getenv('SMTP_HOST'),
        port=os.getenv('SMTP_PORT'),
        username=os.getenv('SMTP_USER'),
        password=os.getenv('SMTP_PASSWORD'),
    )


def get_event_table():
    response = requests.get(
        url=f"{API_URL}/events/xlsx/{EVENT_ID}"
    )
    if response.status_code != 200:
        print(
            response.status_code,
            file=sys.stderr
        )
        return None
    return response.content


if __name__ == "__main__":
    client = get_mail_client()
    client.send(
        subject="Event ticket groups report",
        sender=get_default_sender(),
        receivers=SMTP_TO,
        text="Hi,\n all you need is in attachments.\nHave a nice day.",
        attachments={
            f"cutetix-event-{EVENT_ID}.xlsx": get_event_table()
        }
    )
