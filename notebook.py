import pyautogui as pag
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

keys = 13

x=90
discord_pos = [680,2100]
rl_pos = 1400
rlinsider_pos = 1550
rltracker_pos = 1700
loot_pos = 1840
trade_central_pos = 1260
clickLocations = [rlinsider_pos,loot_pos,trade_central_pos]
duration = 0.001


def sell():
    url = 'https://rl.insider.gg/pc?mobile'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    items = ['Slipstream']

    message = []
    for item in items:
        soup2 = soup.find('div', {'data-itemfullname': item})
        print(soup2.find('span', {'class': 'itemPriceUnpainted'}))
        soup3 = str(soup2.find('span', {'class': 'itemPriceUnpainted'}))
        key = int(re.findall('[0-9]+', soup3)[0])
        message.append(':carrot: **[H]** *' + item + '* **[W]** *' + str(key) + 'k*')

    for server in clickLocations:
        pag.click(x=x, y=server, clicks=1, interval=1, button='left')
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
        pag.click(x=x, y=server, clicks=1, interval=1, button='left')
        for i in message:
            pag.typewrite(i, interval=duration)
            pag.hotkey('shift', '\n')

        pag.typewrite('\n',interval=duration)

    print('finished advertisement', time.localtime())

conf = True
minutes = 10
a = input('buy/sell')
if a == 'buy':
    while True:
            if pag.locateOnScreen('windows_pic.png') is not None:
                if pag.locateOnScreen('discord.png') is not None:
                    print('disocrd located')
                    buy()
                else:
                    print('discord not located')
                    pag.click(x=discord_pos[0], y=discord_pos[1], clicks=1, interval=duration, button='left')
                    buy()
                print('proceeding to long sleep')
                time.sleep(60*minutes)
                print('slept')
            else:
                print('short sleep')
                time.sleep(15)
else:
    while True:
        if pag.locateOnScreen('windows_pic.png') is not None:
            if pag.locateOnScreen('discord.png') is not None:
                print('disocrd located')
                sell()
            else:
                print('discord not located')
                pag.click(x=discord_pos[0], y=discord_pos[1], clicks=1, interval=duration, button='left')
                sell()
            print('proceeding to long sleep')
            time.sleep(60 * minutes)
            print('slept')
        else:
            print('short sleep')
            time.sleep(15)
