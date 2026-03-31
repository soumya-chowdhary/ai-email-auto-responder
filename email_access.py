import imaplib, email

EMAIL = "soumyachowdhary2@gmail.com"
APP_PASSWORD = "mzsn mwcw ffzh urqe"

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, APP_PASSWORD)
mail.select("inbox")

_, msgs = mail.search(None, "ALL")
latest = msgs[0].split()[-1]

_, data = mail.fetch(latest, "(RFC822)")
msg = email.message_from_bytes(data[0][1])

print("From:", msg["From"])
print("Subject:", msg["Subject"])

body = ""
if msg.is_multipart():
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True).decode()
else:
    body = msg.get_payload(decode=True).decode()

print("\nBody:\n", body)

mail.logout()