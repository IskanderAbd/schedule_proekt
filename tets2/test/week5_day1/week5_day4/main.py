import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='grid-list')
    mobiles = catalog.find_all('div', class_='ty-column4')
    # print(mobiles[0].find('img').get('alt'))
    # print(mobiles[0].find('img').get('data-ssrc'))
    for mobile in mobiles:
        try:
            title = mobile.find('img').get('alt')
        except:
            title = ''
    
        try:
            image = mobile.find('img').get('data-ssrc')
        except:
            image = ''

        data = {
            'title': title,
            'image': image
        }
        write_csv(data)

def write_csv(data):
    with open('mobiles.csv', 'a')as csv_file:
        writer = csv.writer(csv_file, delimiter='/')

        writer.writerow(
            (data['title'],
            data['image'])
        )

def main():
    for page in range(1,16):
        print(f'Parsim {page} stranicu')
        url = f'https://svetofor.info/sotovye-telefony-i-aksessuary/vse-smartfony/smartfony-s-podderzhkoy-4g-ru/page-{page}'
        html = get_html(url)
        data = get_data(html)
main()

