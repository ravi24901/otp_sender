from email.message import EmailMessage
import ssl
import smtplib
import random
from sys import argv

def send_mail(email_receiver):
    app_pas=''
    email_sender=''
    if not email_receiver: email_receiver=''

    subject='Securely login with the code'
    otp=otp_generator()
    body='Your security code is {}'.format(otp_generator())

    em=EmailMessage()
    em['From']= email_sender
    em['To']=email_receiver
    em['Subject']=subject
    em.set_content(body)

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,app_pas)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
    return email_receiver,otp

def otp_generator():
    return int(random.randint(100000,999999))


if __name__ == '__main__':
    email_receiver = argv[-1]
    print(send_mail(str(email_receiver)))
