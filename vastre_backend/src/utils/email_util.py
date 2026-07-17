import random
import smtplib
from dotenv import load_dotenv
load_dotenv()
from email.message import EmailMessage
import os

def generate_otp(user_email):
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))

    print(otp)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(str(os.getenv('EMAIL_USER')), str(os.getenv( 'EMAIL_PASSWORD')))
    to_mail = user_email
    from_mail = str(os.getenv('EMAIL_USER'))

    msg = EmailMessage()
    msg["Subject"] = "OTP VERIFICATION"
    msg["From"] = from_mail
    msg["To"] = to_mail

    msg.set_content("your otp is : " + otp)

    server.send_message(msg)
    print("email sent")
    return otp

def verify_otp(user_otp , otp):
    if otp == user_otp:
        return True
    return None