import requests
import csv
import time
from bs4 import BeautifulSoup

def bs_books():
    link = 'https://www.amazon.in/gp/bestsellers/books/'
    csv_file = open('Amazon_Bestsellers.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'Author', 'Type', 'Ratings', 'Number of ratings', 'Price(in rupees)'])

    for i in range(2):
        url = requests.get(link).text
        soup = BeautifulSoup(url, 'lxml')
        items = soup.find_all('div', class_="zg-grid-general-faceout")

        for item in items:
            title = item.find('div', class_="_p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y").text
            author = item.find('div', class_="a-row a-size-small").text
            type_ = item.find('span', class_="a-size-small a-color-secondary a-text-normal").text

            try:
                ratings = item.find('div', class_="a-icon-row").a.i.text
                ratings = float(ratings.split(' ')[0])
            except:
                ratings = None

            try:
                num_of_ratings = item.find('div', class_="a-icon-row").find('span', class_="a-size-small").text.replace(',','')
                num_of_ratings = int(num_of_ratings)
            except:
                num_of_ratings = None

            try:
                price = item.find_all('div', class_="a-row")[3].find('span', class_="a-size-base").text.replace('₹','').replace(',','')
            except:
                price = item.find_all('div', class_="a-row")[2].find('span', class_="a-size-base").text.replace('₹','').replace(',','')
            price = float(price)

            print(title)
            print(author)
            print(type_)
            print(ratings)
            print(num_of_ratings)
            print(price)
            print(' ')
            csv_writer.writerow([title, author, type_, ratings, num_of_ratings, price])

        link = 'https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg=2'

    csv_file.close()

if __name__ == '__main__':
    while True:
        bs_books()
        wait = 60*24
        print('Waiting for 24 hours...')
        time.sleep(wait * 60)
