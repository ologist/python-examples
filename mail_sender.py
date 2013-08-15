import smtplib

class MailSender(object):
    def __init__(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(True)
        server.starttls()
        server.login('ologist0@gmail.com', 'yoon0822')

    def send(sender, receiver, message):
        server.sendmail(sender, receiver, messae)

if __name__ == '__name__':
    sender = MailSender()
    sender.send('ologist0@gmail.com','ologist0@naver.com','test') 
