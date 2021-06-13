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
    anykey = input("Page information is downloaded. Press any key to continue.")

    return(f"""        Район Изгрев 
        
        {date}
        Днес без вода ще бъдат {message}
    """)



regionIzgrev = getWatter(
    region_page='http://www.vikvarna.com/bg/messages/breakdown.html?region_id=15&sub_region_id=22',
    latest_notification='#main_content > div:nth-child(2) > div.list-item-text',
    notification_date= '#main_content > div:nth-child(2) > div.list-item-date')

print(regionIzgrev)

