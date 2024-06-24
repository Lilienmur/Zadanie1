import requests
import time

from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta

def commands(duration_hours):
    end_time = datetime.now() + timedelta(hours=duration_hours)
    print(f'Скрипт запущен на {duration_hours} часов. Время окончания: {end_time}')

    while datetime.now() < end_time:
        print('Первая ссылка идет в обработку')
        url = 'https://democrats.org/'  # Замените на актуальный URL
        parser()
        time.sleep(600)
        print('Новый запуск поиска')
        print("*" * 50)
def parser():
    URL = "https://democrats.org/news/"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find('li', class_ = "posts-list__item")

    title = post.find('h1', class_="posts-list__title").text.strip()
    if 'Democrats' in title or 'democratic' in title or 'Republ' in title or 'Republic' in title or 'republ' in title or 'Republicans' in title or 'Trump' in title or 'Biden' in title:
        print(title)

commands(8)