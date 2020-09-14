import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com" # for gmail. you can choose hotmail or another email services.
sender_email = "sendermail@example.com"
receiver_email = "receivermail@example.com"
password = input("Type your password and press enter:")
message = """\

    Your Message is here.
"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)