import email
import imaplib
import re

from config import EMAIL_ADDRESS, EMAIL_PASSWORD, IMAP_SERVER
from email_service import envoyer_email


def alert_keyword(keyword):
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select("inbox")

    _, messages = mail.search(None, "UNSEEN")

    for eid in messages[0].split():
        _, msg_data = mail.fetch(eid, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])
        body = msg.get_payload(decode=True)

        if body and re.search(keyword, body.decode(errors="ignore"), re.IGNORECASE):
            envoyer_email(
                "System",
                "Alert",
                EMAIL_ADDRESS,
                f"Keyword '{keyword}' found in email: {msg.get('Subject')}",
            )

    mail.logout()
