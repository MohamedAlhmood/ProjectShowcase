import smtplib ,ssl


def sendMail(message):
    host = 'smtp.gmail.com'
    port = 465
    password = 'mmnkrnnrjuyjjdel'
    reciever = 'moealhmood21@gmail.com'
    username= 'moealhmoodcs@gmail.com'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)


