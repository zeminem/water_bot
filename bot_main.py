from email_sending import letter_sending
from ViK import getWatter
import time
from datetime import datetime



def main():
    regionIzgrev = getWatter(
        region_page='http://www.vikvarna.com/bg/messages/breakdown.html?region_id=15&sub_region_id=22',
        latest_notification='#main_content > div:nth-child(2) > div.list-item-text',
        notification_date='#main_content > div:nth-child(2) > div.list-item-date')

    print(letter_sending("""Меденките, доста ви обичкат <3 :* ^.^
    
    
                                                            _____$$$$_________$$$$
                                                            ___$$$$$$$$_____$$$$$$$$
                                                            _$$$$$$$$$$$$_$$$$$$$$$$$$
                                                            $$$$$$$$$$$$$$$$$$$$$$$$$$$
                                                            $$$$$$$$$$$$$$$$$$$$$$$$$$$
                                                            _$$$$$$$$$$$$$$$$$$$$$$$$$
                                                            __$$$$$$$$$$$$$$$$$$$$$$$
                                                            ____$$$$$$$$$$$$$$$$$$$
                                                            _______$$$$$$$$$$$$$
                                                            __________$$$$$$$
                                                            ____________$$$
                                                            _____________$

    
    """))

    now = datetime.now()
    print(f"=> Program finished successfully at /{now}/. <= \n\n")




if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600)
