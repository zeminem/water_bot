import smtplib
from resources.email_list import emails, theone
from resources.key_parts import secret
from email.mime.text import MIMEText


def letter_sending(email_subject):

    to_list = emails  # List of receivers
    content = f"{email_subject}"
    subject = f'Izvestie za vodicata.'

    # abv.bg Fix
    msg = MIMEText(content.encode('utf-8'), 'plain', 'UTF-8')
    msg['From'] = f"{theone}"
    msg['MIME-Version'] = "1.0"
    msg['Subject'] = subject
    msg['Content-Type'] = "text/html; charset=utf-8"
    msg['Content-Transfer-Encoding'] = "quoted-printable"

    #  Process of connection
    conn = smtplib.SMTP('smtp.gmail.com', 587)  # Connection Object. Connecting to the domain of our e-mail server
    conn.ehlo()  # Connecting. Sending Internet traffic from our Python program
    conn.starttls()  # Encrypts the Password that we send to the server

    # Logging and sending the emails
    conn.login(theone, secret)  # Login function
    anykey = input("E-mail log in successful. Press any key to continue.")
    conn.sendmail(theone, to_list, msg.as_string())  # SENDING the e-mails


    return f"Sending e-mails to the following addresses: {to_list}"
