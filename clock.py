import requests
import os
import time
import schedule

from dotenv import load_dotenv

import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from models import Subscrybers, PG_DSN
from weather import get_weather, url


load_dotenv()

token = os.getenv('TOKEN')

BASE_URL = f'https://api.telegram.org/bot{token}/'

class TeleAnswer():
    def __init__(self, token):
        self.token = token
    def send_message(self, chat_id, text):
        url = BASE_URL + "sendMessage"
        param = {
            'chat_id':chat_id,
            'text':text
        }
        requests.post(url, params = param)

def main():


    text = 'Доброе утро! \n' + str(get_weather(url))
    # text = 'тестовая строка '


    DSN = PG_DSN
    engine = sq.create_engine(DSN)
    Session = sessionmaker(bind=engine)
    session = Session()
    data_db = session.query(Subscrybers.subscryber_number).all()
    data_db = tuple(map(lambda x: x[0], data_db))
    bot = TeleAnswer(token)
    [bot.send_message(chat_id=i, text=text) for i in data_db]
    print('SENDED')



if __name__ == '__main__':
    schedule.every().day.at(os.getenv('RING_TIME')).do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)




