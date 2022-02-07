from cgitb import html
from operator import delitem
import re
import requests
from bs4 import BeautifulSoup as BS

import csv

URL = 'https://vesti.kg/'
# HEADERS = {'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'} 
def get_html(url):
    response = requests.get(url)
    return response.text
    

def get_data(html):
    soup = BS(html, 'lxml')
    items = soup.find_all('div', class_="item-Body")

    # print(items)
    
    for news in items:
        
        try:
            title = news.find('h2', class_='title').text.strip()
        except:
            title = ''
        
           
 
        data = {
            'title': title,
            
        }
        write_csv(data)

def write_csv(data):
    with open('cars.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')

        writer.writerow(
            (
                data['title'],
                
            )
        )

def main():
    for page in range(33):
        print(f'Парсинг {page + 1}  страницы...')
        url = 'https://vesti.kg/itemlist.html?start=78750{page}'
        html = get_html(url)
        get_data(html)
        
main()