import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "turquase.development@gmail.com"
receiver_email = "xdfuu.blockchain@zohomail.com"
password = input("Type your password and press enter:")
message = """\
Subject: Riot Games Username Assistance
Username Assistance
Below you will find the accounts associated with your email address: oxobis58@gmail.com.
Riot Account username(s) associated with a League of Legends region

Turkey
highdose558



GLHF,
Riot Games

"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)