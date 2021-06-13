import bs4
import requests
import smtplib



theone = 'medo.istesting@gmail.com'
emails = ['zeminem@abv.bg', 'medo.istesting@gmail.com'] #'z.cholakova@abv.bg'
secret = 'iamtestingR35'

def getWatter(region_page, latest_notification, notification_date):
    res = requests.get(region_page)
    # res.raise_for_status()
    res.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    notification_element = soup.select(latest_notification)
    date_element = soup.select(notification_date)

    message = notification_element[0].text.strip()
    date = date_element[0].text.strip()
    anykey = input("\n=>  Page information is downloaded. Press any key to continue.")

    return (f"""        Район Изгрев 

        {date}
        Днес без вода ще бъдат {message}
    """)



def letter_sending(email_subject):

    to_list = emails  # List of receivers

    #  Process of connection
    conn = smtplib.SMTP('smtp.gmail.com', 587)  # Connection Object. Connecting to the domain of our e-mail server
    conn.ehlo()  # Connecting. Sending Internet traffic from our Python program
    conn.starttls()  # Encrypts the Password that we send to the server

    # Logging and sending the emails
    conn.login(theone, secret)  # Login function

    anykey = input("\n=> E-mail log in successful. Press any key to continue.")
    print(f"\n=> Sending e-mails to the following addresses: {to_list}")
    conn.sendmail(theone, to_list, f'Subject: Izvestie za vodicata...\n\n{email_subject}')  # SENDING the e-mails


    return f"\nE-mails have been sent."



def main():
    regionIzgrev = getWatter(
        region_page='http://www.vikvarna.com/bg/messages/breakdown.html?region_id=15&sub_region_id=22',
        latest_notification='#main_content > div:nth-child(2) > div.list-item-text',
        notification_date='#main_content > div:nth-child(2) > div.list-item-date')

    print(letter_sending(regionIzgrev))

    anykey = input("\n=> Program finished successfully. Press any key to Close.")

    return anykey



if __name__ == "__main__":
    print(main())
