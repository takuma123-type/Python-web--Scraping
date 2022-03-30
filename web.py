from bs4 import BeautifulSoup
import requests

url_ec = 'https://scraping.official.ec/'
res =  requests.get(url_ec)
soup = BeautifulSoup(res.text, 'html.parser')
item_list = soup.find('ul', {'id': 'itemList'})
items = item_list.find_all('li')

data_ec = []
for item in items:
    datum_ec = {}
    datum_ec['title'] = item.find('p', {'class': 'items-grid_itemTitleText_b58666da'}).text
    price = item.find('p', {'class': 'items-grid_price_b58666da'}).text
    datum_ec['price'] = int(price.replace('¥', '').replace(',', ''))
    datum_ec['link'] = item.find('a')['href']
    is_stock = item.find('p', {'class': 'items-grid_soldOut_b58666da'}) == None
    datum_ec['is_stock'] = '在庫あり' if is_stock == True else '在庫なし'
    data_ec.append(datum_ec)
    print(data_ec)