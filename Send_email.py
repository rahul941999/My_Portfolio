import smtplib
import ssl
import os

host = 'smtp.elasticemail.com'
port = 2525
user_name = "rahul941999@gmail.com"
password = os.getenv("ElasticeEmail")
receiver = "rahul941999@yahoo.com"
context = ssl.create_default_context()


def send(subject, txt):
    message = 'Subject: {}\n\n{}\n\n'.format(subject, txt)
    with smtplib.SMTP(host=host, port=port) as server:
        server.login(user=user_name, password=password)
        server.sendmail(from_addr=user_name, to_addrs=receiver, msg=message)
