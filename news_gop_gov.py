import requests
import time

from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta

def commands(duration_hours):
    start_time = datetime.now()
    end_time = datetime.now() + timedelta(hours=duration_hours)
    print(f'Скрипт запущен на {duration_hours} часов. Время старта: {start_time}Время окончания: {end_time}')
    while datetime.now() < end_time:
        print('Первая ссылка идет в обработку')
        url = 'https://democrats.org/'# Замените на актуальный URL

        parser()
        time.sleep(600)
        print('Новый запуск поиска')
        print("*" * 50)
def parser():
    URL = "https://www.nbcnews.com/politics"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find('div', class_ = "wide-tease-item__info-wrapper flex-grow-1-m")
    # print(post)
    url = post.a['href']

    title = post.find('h2', class_="wide-tease-item__headline").text.strip()
    # print(title)
    if 'Democrats' in title or 'democrat' in title or 'Democratic' in title or 'democratic' in title or 'Republ' in title or 'Republic' in title or 'republ' in title or 'Republicans' in title or 'Trump' in title or 'Biden' in title or 'GOP' in title:
        print(title)
        print(url)


commands(8)