#!/usr/bin/python3
"""Email sorting program"""
import os
import imaplib


def sort_emails():
# Email account credentials
    email = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD")
    imap_url = "imap.gmail.com"


    # Connect to the email server
    mail = imaplib.IMAP4_SSL(imap_url)
    mail.login(email, password)
    mail.select("inbox") # select the inbox to search

    #search for emails from specific sender
    status, messages = mail.search(None, '(UNSEEN FROM "do-not-reply@updates.funko.com")')
    if status != "OK":
        print("No messages found.")
        exit()

    # Move emails to another folder
    for num in messages[0].split():
        mail.store(num, '+X-GM-LABELS', 'Sorted') # For Gmail

    mail.expunge()
    mail.close()

    print("Emails sorted successfully!")

sort_emails()