from requests_html import HTML, HTMLSession
import csv

csv_file = open('scrape_csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'price', 'stock', 'url'])

session = HTMLSession()
r = session.get('https://books.toscrape.com/')

books = r.html.find('.product_pod')

for book in books:
    title = book.find('h3 a')[0].attrs['title'] # Título del libro
    price = book.find('.price_color')[0].text # Precio del libro
    stock = book.find('.instock.availability')[0].text # Disponibilidad del libro
    url_id = book.find('h3 a')[0].attrs['href'] # Extraigo el enlace HTML relativo
    url = f'https://books.toscrape.com/{url_id}' # Armo el enlace completo
    print(f'Título: {title}')
    print(f'Precio: {price}')
    print(f'Disponibilidad: {stock}')
    print(f'URL: {url}')
    print()
    csv_writer.writerow([title, price, stock, url])

csv_file.close()
