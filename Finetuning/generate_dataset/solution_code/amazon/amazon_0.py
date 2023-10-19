import csv
from bs4 import BeautifulSoup

def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    product_data = []
    product_names = soup.find_all('span', class_='a-text-normal')
    product_prices = soup.find_all('span', class_='a-offscreen')
    shipping_dates = soup.find_all('span', class_='a-text-bold')
    
    for name, price, date in zip(product_names, product_prices, shipping_dates):
        data = {
            'Product Name': name.get_text(strip=True),
            'Price': price.get_text(strip=True),
            'Shipping Date': date.get_text(strip=True)
        }
        product_data.append(data)
    
    return product_data

def save_to_csv(data, filename):
    keys = data[0].keys()
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

html_file = 'downloaded_pages/amazon.com.html'
output_file = 'scraped_data.csv'

with open(html_file, 'r') as file:
    html = file.read()

data = extract_data(html)
save_to_csv(data, output_file)