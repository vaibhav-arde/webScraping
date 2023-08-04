import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging

flipcart_url = "https://www.flipkart.com/search?q=" + "iphone12pro"
urlclient = urlopen(flipcart_url)
flipcart_page = urlclient.read()
flipcart_html = bs(flipcart_page, 'html.parser')
bigboxes = flipcart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
print(len(bigboxes))
del bigboxes[0:2]
del bigboxes[-3:]
print(len(bigboxes))
box = bigboxes[len(bigboxes)-1]
# print(box)
# print(box.div.div.div.a['href'])
for i in bigboxes:
    print("https://flipkart.com" + i.div.div.div.a['href'])

