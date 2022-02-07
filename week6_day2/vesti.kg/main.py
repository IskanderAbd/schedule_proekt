import requests from bs4
from bs4 import BeautifulSoup as BS

def get_htm(url)
    pass

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', id=)