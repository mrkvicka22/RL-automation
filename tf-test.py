import pyautogui as pag
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

keys = 4

rl_pos = [30,560]
rlinsider_pos = (30, 620)
rltracker_pos = (30,670)
loot_pos = (30, 740)
trade_central_pos = (30, 500)
clickLocations = [rlinsider_pos,loot_pos,trade_central_pos]
duration = 0.001


def sell():
    url = 'https://rl.insider.gg/pc?mobile'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    items = ['Slipstream', 'Slipstream', 'Tora']

    message = []
    for item in items:
        soup2 = soup.find('div', {'data-itemfullname': item})
        print(soup2.find('span', {'class': 'itemPriceUnpainted'}))
        soup3 = str(soup2.find('span', {'class': 'itemPriceUnpainted'}))
        key = int(re.findall('[0-9]+', soup3)[0])
        message.append(':carrot: **[H]** *' + item + '* **[W]** *' + str(key) + 'k*')

    for server in clickLocations:
        pag.click(x=server[0], y=server[1], clicks=1, interval=1, button='left')
        for i in message:
            pag.typewrite(i, interval=duration)
            pag.hotkey('shift', '\n')

        pag.typewrite('\n',interval=duration)

    print('finished advertisement', time.localtime())


def buy():
    url = 'https://rl.insider.gg/pc?mobile'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    items = ['Intrudium', 'Dissolver', 'Chameleon', 'Fire God', 'Bubbly', 'Streamline', 'Trigon', 'Heatwave', '20xx',
             'Parallax', 'Labyrinth', 'Slipstream']
    message = []
    for item in items:
        soup2 = soup.find('div', {'data-itemfullname': item})
        print(soup2.find('span', {'class': 'itemPriceUnpainted'}))
        soup3 = str(soup2.find('span', {'class': 'itemPriceUnpainted'}))
        key = int(re.findall('[0-9]+', soup3)[0]) - 1
        if keys >= key:
            message.append(':carrot: **[H]** *' + str(key) + 'k* **[W]** *' + item + '*')

    for server in clickLocations:
        pag.click(x=server[0], y=server[1], clicks=1, interval=1, button='left')
        for i in message:
            pag.typewrite(i, interval=duration)
            pag.hotkey('shift', '\n')

        pag.typewrite('\n',interval=duration)

    print('finished advertisement', time.localtime())


minutes = 10
a = input('buy/sell')
if a == 'buy':
    while True:
        try:
            pag.locateCenterOnScreen('windows_pic.png')
            try:
                pag.locateCenterOnScreen('servery.png')
                buy()
                print('proceeding to long sleep')
                time.sleep(60 * minutes)
                print('long sleep ended')
            except TypeError:
                pag.click(x=855, y=1060, clicks=1, interval=duration, button='left')
                buy()
                print('proceeding to long sleep')
                time.sleep(60 * minutes)
                print('long sleep ended')
        except TypeError:
            time.sleep(30)
            print('sleeped')
else:
    while True:
        try:
            pag.locateCenterOnScreen('windows_pic.png')
            try:
                pag.locateCenterOnScreen('servery.png')
                sell()
                print('proceeding to long sleep')
                time.sleep(60 * minutes)
                print('long sleep ended')
            except TypeError:
                pag.click(x=855, y=1060, clicks=1, interval=duration, button='left')
                sell()
                print('proceeding to long sleep')
                time.sleep(60 * minutes)
                print('long sleep ended')
        except TypeError:
            time.sleep(30)
            print('sleeped')
