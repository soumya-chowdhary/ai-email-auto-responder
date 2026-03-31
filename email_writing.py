import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL = "soumyachowdhary2@gmail.com"
APP_PASSWORD = "xxzc qvyz yywy otqv"

to_email = "jiyaarorahmh@gmail.com"

msg = MIMEMultipart()
msg["From"] = EMAIL
msg["To"] = to_email
msg["Subject"] = "Test Mail from Python"

body = "Hello"
msg.attach(MIMEText(body, "plain"))

# Connect SMTP
smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.starttls()
smtp.login(EMAIL, APP_PASSWORD)

smtp.send_message(msg)
smtp.quit()

print("Mail sent successfully ")