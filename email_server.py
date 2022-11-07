import smtplib

class EmailServer:
    def __init__(self, to_email, subject, body) -> None:
        self.to_email = to_email
        self.subject = subject
        self.body = body

    def sendMail(self):
        print('ENVIANDO E-MAIL PARA: ',self.to_email)
        mail_from = 'mt4@focus.com' #from email
        mail_to = self.to_email
        mail_subject = self.subject
        mail_message_body = self.body

        mail_to_string = ', '.join(mail_to)

        server = smtplib.SMTP('127.0.0.1') #SMTP server
        server.sendmail(mail_from, mail_to, mail_subject, mail_message_body)
        server.quit()