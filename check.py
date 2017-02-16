import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.infibeam.com/deal-of-the-day/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
f = urllib.request.urlopen(req)
soup = BeautifulSoup(f, 'html.parser')
#get all items' price
all_item_price = soup.findAll("div", { "class" : "final-price" })
all_item_prices = [x.find('span', {"class" : "price"}).text for x in all_item_price]
#get all items' name and link
mb_items_all = soup.findAll("h1", { "class" : "product-title-big" })
item_names = [x.find('a').text for x in mb_items_all]
all_item_names = item_names[::2]
item_links = [x.find('a')['href'] for x in mb_items_all]
all_item_links = item_links[::2]