import requests
import os
from dotenv import load_dotenv
load_dotenv()


url = f"https://api.weather.yandex.ru/v2/forecast?lat={os.getenv('LAT')}&lon={os.getenv('LON')}"

def get_weather(url):

    result = requests.get(url=url, headers={'X-Yandex-API-Key': os.getenv('YA')}).json()
    root = result['forecasts'][0]['parts']
    weather = f'''Сегодня: {result['forecasts'][0]['date']},
погода утром: {root['morning']['temp_avg']}c, явления: {root['morning']['condition']} 
погода днём: {root['day']['temp_avg']}c, явления: {root['day']['condition']} 
погода вечером: {root['evening']['temp_avg']}c, явления: {root['evening']['condition']} 
погода ночью: {root['night']['temp_avg']}c, явления: {root['night']['condition']}'''

    return weather


