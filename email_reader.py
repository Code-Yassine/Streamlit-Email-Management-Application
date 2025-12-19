import email
import imaplib
import re

from config import EMAIL_ADDRESS, EMAIL_PASSWORD, IMAP_SERVER


def get_5_unread_emails():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select("inbox")

    _, messages = mail.search(None, "UNSEEN")
    email_ids = messages[0].split()[-5:]

    results = []
    for eid in email_ids:
        _, msg_data = mail.fetch(eid, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])
        results.append(
            {
                "From": msg.get("From"),
                "Subject": msg.get("Subject"),
                "Date": msg.get("Date"),
            }
        )

    mail.logout()
    return results


def filter_emails(sender=None, subject=None, regex=None):
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select("inbox")

    _, messages = mail.search(None, "ALL")
    results = []

    for eid in messages[0].split():
        _, msg_data = mail.fetch(eid, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body += part.get_payload(decode=True).decode(errors="ignore")
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")

        if sender and sender not in msg.get("From", ""):
            continue
        if subject and subject not in msg.get("Subject", ""):
            continue
        if regex and not re.search(regex, body, re.IGNORECASE):
            continue

        results.append(msg.get("Subject"))

    mail.logout()
    return results
