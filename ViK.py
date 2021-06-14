import bs4
import requests


def getWatter(region_page, latest_notification, notification_date):
    res = requests.get(region_page)
    # res.raise_for_status()
    res.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    notification_element = soup.select(latest_notification)
    date_element = soup.select(notification_date)

    message = notification_element[0].text.strip()
    date = date_element[0].text.strip()
    ##anykey = input("\n=> Page information is downloaded. Press any key to continue.")

    email_notification = (f"""        Район Изгрев 
        
        {date}
        Днес без вода ще бъдат {message}
    """)


    return email_notification



