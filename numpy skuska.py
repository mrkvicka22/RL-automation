import requests
from bs4 import BeautifulSoup
from bs4 import Tag
import re

url = 'https://rl.insider.gg/pc?mobile'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = ['Slipstream', 'Tora', 'Mainframe']
message = []
soup = soup.find('div', {'id':'contentContainer'})
soup = soup.find('div', {'id':'itemPricesContainer'})
bujony = soup.find_all('div',{'class': 'priceTableContainer'})
soups = soup.find_all('div',{'class': 'priceTableContainer unpaintable'})
for item in items:
    for soup in soups:
        soup2 = soup.find('div', {'data-itemfullname': item})
        if soup2 is not None:
            soup3 = str(soup2.find('span', {'class': 'itemPriceUnpainted'}))
            key = int(re.findall('[0-9]+', soup3)[0])
            message.append(':carrot: **[H]** *' + item + '* **[W]** *' + str(key) + 'k*')

for item in items:
    for bujon in bujony:
        bujon = bujon.find('div', {'class':'itemPicsContainer'})
        bujon2 = bujon.find('div', {'data-itemfullname': item})
        print(bujon2)
        if bujon2 is not None:
            tag = bujon2.div
            prices = list(eval(tag['data-prices']))
            message.append(':carrot: **[H]** *' + item + '* **[W]** *' + str(prices[0]) + 'k*')


print(message)
