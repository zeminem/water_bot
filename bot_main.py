
from email_sending import letter_sending
from ViK import getWatter


def main():
    regionIzgrev = getWatter(
        region_page='http://www.vikvarna.com/bg/messages/breakdown.html?region_id=15&sub_region_id=22',
        latest_notification='#main_content > div:nth-child(2) > div.list-item-text',
        notification_date='#main_content > div:nth-child(2) > div.list-item-date')

    print(letter_sending(regionIzgrev))

    anykey = input("Program finished successfully. Press any key to Close.")

    return anykey



if __name__ == "__main__":
    print(main())
