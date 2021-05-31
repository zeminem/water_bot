import smtplib
from resources.email_list import emails, theone
from resources.key_parts import secret

def letter_sending(email_subject):

    to_list = emails  # List of receivers

    #  Process of connection
    conn = smtplib.SMTP('smtp.gmail.com', 587)  # Connection Object. Connecting to the domain of our e-mail server
    conn.ehlo()  # Connecting. Sending Internet traffic from our Python program
    conn.starttls()  # Encrypts the Password that we send to the server

    # Logging and sending the emails
    conn.login(theone, secret)  # Login function
    conn.sendmail(theone, to_list, f'Subject: Izvestie za vodicata...\n\n{email_subject}')  # SENDING the e-mails


    return f"Sending e-mails to the following addresses: {to_list}"
