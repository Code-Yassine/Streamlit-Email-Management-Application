# 📧 Streamlit Email Management Application

This project is a **modular Python + Streamlit web application** for managing emails securely and efficiently.

The application allows users to:
- Send emails with attachments
- View the 5 latest unread emails
- Apply advanced filters (sender, subject, regex)
- Receive automatic email alerts based on keywords

The project follows **best practices** such as modular architecture and secure handling of secrets using environment variables.

---

## 📁 Project Structure
```
email-streamlit-app/
│
├── app.py # Streamlit UI (main entry point)
├── config.py # Configuration & environment variables
├── email_service.py # Send emails (SMTP)
├── email_reader.py # Read & filter emails (IMAP)
├── alert_service.py # Alert system
├── email_archiver.py # Archive emails
├── requirements.txt
├── README.md
├── .env # Secrets (NOT pushed to GitHub)
└── .gitignore
```


---

## 🚀 Features

### ✉️ Send Email
- Enter destination email
- Write a message
- Attach a file (optional)

### 📥 Read Emails
- Display **only the 5 latest unread emails**
- Show sender, subject, and date

### 🔍 Advanced Filtering
- Filter by sender
- Filter by subject
- Search using **regular expressions** in the email body

### 🗃️ Email Archiving
- Archive emails based on criteria
- Manage archived emails

### 🚨 Alert System
- Monitor unread emails
- Automatically send an alert email when a keyword is detected

---

## 🧰 Technologies Used
- Python 3
- Streamlit
- SMTP & IMAP
- Regular Expressions
- python-dotenv
- Environment Variables

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 🔐 Environment Variables (IMPORTANT)

Create a .env file in the project root directory:
```bash
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_google_app_password
```
### ▶️ Run the Application
```bash
streamlit run app.py
```
