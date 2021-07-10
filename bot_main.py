from email_sending import letter_sending
from scraper import scrape_vik
import time
from datetime import datetime


def main():
    # Scrape the VIK website for the latest notification
    print(f"\n=> Scraping the website data.<=")
    region_izgrev = scrape_vik(
        region_page='http://www.vikvarna.com/bg/messages/breakdown.html?region_id=15&sub_region_id=22',
        latest_notification='#main_content > div:nth-child(2) > div.list-item-text',
        notification_date='#main_content > div:nth-child(2) > div.list-item-date')
    # PAUSE
    time.sleep(2)

    # Calling the function for sending out e-mails to the list of recipients
    letter_sending(region_izgrev)
    print(f"\n=> Sending e-mails to all users from the list.<=")
    # PAUSE
    time.sleep(0.8)
    print("\n       Emails have been sent.")
    # PAUSE
    time.sleep(2)

    # Just a fun little count off to end the program
    now = datetime.now()
    print(f"\n=> Program finished successfully at /{now}/. <=")
    print("\nShutting down in...")
    counter = 5
    for i in range(0, 5):
        print(f"                {counter}")
        counter = counter - 1
        time.sleep(0.95)
    print("\nTURNING OFF")
    # PAUSE
    time.sleep(0.8)


if __name__ == "__main__":
    while True:
        main()
        exit()
