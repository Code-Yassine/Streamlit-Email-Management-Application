import email
import imaplib
import os

from config import ARCHIVE_DIR, EMAIL_ADDRESS, EMAIL_PASSWORD, IMAP_SERVER


def archive_email(email_id, category):
    """
    Archive an email into a category folder (factures, personnel, projets, etc.)
    """
    category_path = os.path.join(ARCHIVE_DIR, category)
    os.makedirs(category_path, exist_ok=True)

    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select("inbox")

    _, msg_data = mail.fetch(email_id, "(RFC822)")
    file_path = os.path.join(category_path, f"{email_id.decode()}.eml")

    with open(file_path, "wb") as f:
        f.write(msg_data[0][1])

    mail.logout()
    return file_path
