import streamlit as st
from alert_service import alert_keyword
from archive_service import archive_email
from email_reader import filter_emails, get_5_unread_emails
from email_service import envoyer_email

st.set_page_config(page_title="Email App", layout="wide")
st.title("📧 Email Management Application")

# ===================== SIDEBAR =====================
menu = st.sidebar.radio(
    "📂 Navigation",
    [
        "✉️ Send Email",
        "📥 View 5 Unread Emails",
        "🔍 Filter Emails",
        "📦 Archive Emails",
        "🚨 Alert System",
    ],
)

# ===================== SEND EMAIL =====================
if menu == "✉️ Send Email":
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
        st.success("✅ Email sent successfully")

# ===================== VIEW EMAILS =====================
elif menu == "📥 View 5 Unread Emails":
    st.header("📥 Last 5 Unread Emails")

    emails = get_5_unread_emails()
    if emails:
        for e in emails:
            st.markdown(f"""
            **From:** {e["From"]}
            **Subject:** {e["Subject"]}
            **Date:** {e["Date"]}
            ---
            """)
    else:
        st.info("No unread emails")

# ===================== FILTER =====================
elif menu == "🔍 Filter Emails":
    st.header("🔍 Advanced Filter")

    sender = st.text_input("Filter by sender")
    subject = st.text_input("Filter by subject")
    regex = st.text_input("Regex in body")

    if st.button("Apply filter"):
        results = filter_emails(sender or None, subject or None, regex or None)

        if results:
            for r in results:
                st.write("✔", r)
        else:
            st.info("No matching emails")

# ===================== ARCHIVE =====================
elif menu == "📦 Archive Emails":
    st.header("📦 Archive Emails by Category")

    emails = get_5_unread_emails()

    if emails:
        email_map = {f"{e['Subject']} ({e['From']})": e["ID"] for e in emails}

        selected_email = st.selectbox("Select email to archive", email_map.keys())

        category = st.selectbox(
            "Choose category", ["factures", "personnel", "projets", "custom"]
        )

        if category == "custom":
            category = st.text_input("Enter custom category name")

        if st.button("Archive Email"):
            path = archive_email(email_map[selected_email], category)
            st.success(f"📁 Email archived in: {path}")
    else:
        st.info("No unread emails to archive")

# ===================== ALERT =====================
elif menu == "🚨 Alert System":
    st.header("🚨 Alert System")

    keyword = st.text_input("Keyword to monitor")

    if st.button("Activate alert"):
        alert_keyword(keyword)
        st.success("✅ Alert check completed")
