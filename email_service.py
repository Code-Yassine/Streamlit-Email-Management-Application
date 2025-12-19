import os
import smtplib
from email.message import EmailMessage

from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_PORT, SMTP_SERVER


def envoyer_email(nom, prenom, destinataire, message, fichier_path=None):
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = destinataire
    msg["Subject"] = f"Message pour {prenom} {nom}"
    msg.set_content(message)

    if fichier_path and os.path.exists(fichier_path):
        with open(fichier_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=os.path.basename(fichier_path),
            )

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
