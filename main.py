import telebot
import os

from dotenv import load_dotenv

import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models import Subscrybers, PG_DSN
from weather import get_weather, url


load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['start'])
def start(message):
    DSN = PG_DSN
    engine = sq.create_engine(DSN)
    Session = sessionmaker(bind=engine)
    session = Session()
    data_db = session.query(Subscrybers.subscryber_number).all()
    data_db = tuple(map(lambda x: x[0] , data_db))
    sub_get = message.chat.id
    if sub_get in data_db:
        bot.send_message(sub_get, "Ты уже подписан")
    else:
        sub = Subscrybers(subscryber_number=sub_get)
        session.add(sub)
        bot.send_message(message.chat.id, "Привет, ты подписался на погоду в Краснодаре")
        session.commit()
        session.close()



@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.chat.id, text=get_weather(url))

@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(message.chat.id, "Я работаю")

@bot.message_handler(commands=['time'])
def ping(message):
    alarm = int(os.getenv('RING_TIME').split(':')[0])
    now = datetime.now().hour
    if now >= alarm:
        time = 24-int(now)+int(alarm)
    else:
        time = alarm-now


    bot.send_message(message.chat.id, f"До будильника осталось {time} часов")

@bot.message_handler(commands=['help'])
def ping(message):
    text = '''/time - показывает сколько часов осталось до будильника
/ping - проверяет работоспособность сервиса
/weather - принудительно проверяет погоду 
/start - добавляет подписчиков'''
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)





