import streamlit as st
from alert_service import alert_keyword
from email_reader import filter_emails, get_5_unread_emails
from email_service import envoyer_email

st.set_page_config(page_title="Email App", layout="centered")
st.title("📧 Email Management Application")

# SEND EMAIL
st.header("✉️ Send Email")
nom = st.text_input("Last Name")
prenom = st.text_input("First Name")
destinataire = st.text_input("Destination Email")
message = st.text_area("Message")
fichier = st.file_uploader("Attachment (optional)")

if st.button("Send Email"):
    path = None
    if fichier:
        path = fichier.name
        with open(path, "wb") as f:
            f.write(fichier.getbuffer())

    envoyer_email(nom, prenom, destinataire, message, path)
    st.success("Email sent successfully")

# READ EMAILS
st.divider()
st.header("📥 Last 5 Unread Emails")

if st.button("Show unread emails"):
    emails = get_5_unread_emails()
    st.table(emails)

# FILTER
st.divider()
st.header("🔍 Advanced Filter")
sender = st.text_input("Filter by sender")
subject = st.text_input("Filter by subject")
regex = st.text_input("Regex in body")

if st.button("Apply filter"):
    results = filter_emails(sender or None, subject or None, regex or None)
    for r in results:
        st.write("✔", r)

# ALERT
st.divider()
st.header("🚨 Alert System")
keyword = st.text_input("Keyword")

if st.button("Activate alert"):
    alert_keyword(keyword)
    st.success("Alert check completed")
