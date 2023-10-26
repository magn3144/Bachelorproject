import csv
from bs4 import BeautifulSoup

def get_category(page, elements):
    soup = BeautifulSoup(page, 'html.parser')
    category_element_xpath = elements.get('category')
    category_element = soup.select_one(category_element_xpath)
    category = category_element.text.strip()
    return category

def scrape_page(page_path, elements):
    with open(page_path, 'r') as file:
        page = file.read()
    category = get_category(page, elements)

    data = {'Category': category}

    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)