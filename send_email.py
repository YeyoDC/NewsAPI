import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "tylerskyler95@gmail.com"
    password = "rrmp vvbh eaxk jzjt"

    receiver = "tylerskyler95@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)