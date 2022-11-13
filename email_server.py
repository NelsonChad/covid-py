import smtplib, ssl
from email.message import EmailMessage

class EmailServer:
    def __init__(self, to_email, subject, body) -> None:
        self.to_email = to_email
        self.subject = subject
        self.body = body

    def sendMail(self):
        try:
            email_address = '' #email do server SMTP
            email_password = '' #senha do email

            if email_address is None or email_password is None:
                # no email address or password
                # something is not configured properly
                print("Configure um email e uma senha?")
                return False

            # create email
            msg = EmailMessage()
            msg['Subject'] = self.subject
            msg['From'] = email_address
            msg['To'] = self.to_email
            msg.set_content(self.body)

            # send email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(email_address, email_password)
                smtp.send_message(msg)
            return True
        except Exception as e:
            print("Problema ao enviar email")
            print(str(e))
        return False