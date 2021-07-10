import bs4
import requests


def scrape_vik(region_page, latest_notification, notification_date):

    # Scrape the given web page
    res = requests.get(region_page)
    res.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Extracting and formatting the notification message and date
    notification_element = soup.select(latest_notification) # Getting the latest notification message
    date_element = soup.select(notification_date) # Getting the date of the notification
    message = notification_element[0].text.strip()
    date = date_element[0].text.strip()


    # String that gets passed to the e-mail sending function
    email_notification = (f"""        Район Изгрев 
        
        {date}
        Днес без вода ще бъдат {message}
    """)


    return email_notification



