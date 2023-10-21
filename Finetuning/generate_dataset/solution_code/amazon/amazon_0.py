import csv
from bs4 import BeautifulSoup

html_file = "downloaded_pages/amazon.html"

def extract_product_info(html):
    soup = BeautifulSoup(html, "html.parser")
    
    product_elements = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")
    price_elements = soup.find_all("span", class_="a-offscreen")
      
    products = [element.get_text(strip=True) for element in product_elements]
    prices = [element.get_text(strip=True) for element in price_elements]
    
    return products, prices

def save_to_csv(data):
    products, prices = data
    
    with open("scraped_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "Price"])
        
        for product, price in zip(products, prices):
            writer.writerow([product, price])

with open(html_file, "r") as file:
    html = file.read()
    data = extract_product_info(html)
    save_to_csv(data)