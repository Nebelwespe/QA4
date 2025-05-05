# send_email.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from env_loader import EMAIL_ADDRESS, EMAIL_PASSWORD, RECIPIENT_EMAIL

def send_email(subject, html_content):
    """
    Sends an HTML email to the recipient defined in the .env file.
    """
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECIPIENT_EMAIL

    # Attach HTML body
    html_part = MIMEText(html_content, "html")
    msg.attach(html_part)

    try:
        print("📤 Connecting to Gmail SMTP server...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())
        print(f"✅ Email sent to {RECIPIENT_EMAIL}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
