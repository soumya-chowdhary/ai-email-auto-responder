import imaplib
import email
from email.message import EmailMessage
import smtplib
from datetime import datetime, time
from google import genai

# ================= CONFIG =================

IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_ID = ".env"
EMAIL_APP_PASSWORD = ".env"

GEMINI_API_KEY = ".env"

# Allowed senders
ALLOWED_SENDERS = [
    "abhimanyududichoudhary@gmail.com",
    "jiyaarorahmh@gmail.com",
    "chowdharybhavya54@gmail.com"]

# Working hours (24 hour format)
WORK_START = time(9, 0, 0)   # 09:00 AM
WORK_END   = time(23, 30, 0)  # 06:00 PM

# =========================================

client = genai.Client(api_key=GEMINI_API_KEY)

# ---------- Time Check ----------
def is_working_hours():
    now = datetime.now().time()
    return WORK_START <= now <= WORK_END

def generate_polite_reply(mail_body):

    prompt = f"""
    You a professional email assistant.
Write a short, polite and helpful reply for this email.
Be respectful and professional.

Email:
{mail_body}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if hasattr(response, "text") and response.text:
            return response.text
        else:
            return "Thank you for your email."

    except Exception as e:
        print("LLM Error:", e)
        return "Thank you for your email. I will get back to you soon."

# ---------- Main Function ----------
def reply_to_latest_email():

    # Check working hours
    if not is_working_hours():
        print(" Not in working hours. No reply sent.")
        return

    # ---------- LOGIN IMAP ----------
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ID, EMAIL_APP_PASSWORD)
    mail.select("inbox")

    # ---------- FETCH UNREAD MAIL ----------
    status, data = mail.search(None, "UNSEEN")
    mail_ids = data[0].split()

    if not mail_ids:
        print("No unread emails.")
        return

    latest_id = mail_ids[-1]

    status, msg_data = mail.fetch(latest_id, "(RFC822)")
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    from_email = email.utils.parseaddr(msg["From"])[1]
    subject = msg["Subject"] or "No Subject"

    print("Latest email from:", from_email)

    # ---------- Sender Filter ----------
    if from_email not in ALLOWED_SENDERS:
        print("Sender not allowed. No reply sent.")
        return

    # ---------- READ BODY ----------
    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode(errors="ignore")
                break
    else:
        body = msg.get_payload(decode=True).decode(errors="ignore")

    # ---------- Generate Reply ----------
    reply_text = generate_polite_reply(body)

    print(" Reply Generated")

    # ---------- SEND MAIL ----------
    reply_msg = EmailMessage()
    reply_msg["From"] = EMAIL_ID
    reply_msg["To"] = from_email
    reply_msg["Subject"] = "Re: " + subject
    reply_msg.set_content(reply_text)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ID, EMAIL_APP_PASSWORD)
        server.send_message(reply_msg)

    print(" Reply Sent!")


# ---------- RUN ----------
reply_to_latest_email()