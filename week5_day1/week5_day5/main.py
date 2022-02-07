import requests
from bs4 import BeautifulSoup as BS

import csv

def get_html(url):
    response = requests.get(url)
    # print(response.status_code)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='browse-view')
    notebooks = catalog.find_all('div', class_ = 'row')
    # print(notebooks[0].find('div', class_='rows').find('a').text.strip()) #title
    # print('https://enter.kg' + notebooks[0].find('a', class_='product-image-link').find('img').get('src')) #img
    # print(notebooks[0].find('span', class_='price').text.strip()) #price

    for note in notebooks:
        try:
            title = note.find('div', class_='rows').find('a').text.strip()
        except:
            title = ''
        try:
            img = 'https://enter.kg' + note.find('a', class_='product-image-link').find('img').get('src')
        except:
            img = ''
        try:
            price = note.find('span', class_='price').text.strip()
        except:
            price = ''

        data = {
            'title': title,
            'img': img,
            'price': price
        }
        
        write_csv(data)

    

def write_csv(data):
    with open('enter_notebooks.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')

        writer.writerow(
            (
                data['title'],
                data['img'],
                data['price']
            )
        )

def main():
    page = 0
    while page<11:
        print(f'Parsing {page +1} stranicy...')
        if page == 0:
            url = 'https://enter.kg/computers/noutbuki_bishkek'
        else:
            url = f'https://enter.kg/computers/noutbuki_bishkek/results,{page}01-{page}00'
        html = get_html(url)
        get_data(html)
        page += 1


main()