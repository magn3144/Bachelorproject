import csv
from bs4 import BeautifulSoup


def extract_bulk_laptop_dealers(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    bulk_laptop_dealers = []

    # Find all the <a> elements that contain 'Bulk Laptop Dealers' in the text
    dealers = soup.find_all('a', text='Bulk Laptop Dealers')
    for dealer in dealers:
        dealer_name = dealer.text
        dealer_link = dealer['href']
        bulk_laptop_dealers.append((dealer_name, dealer_link))
    
    return bulk_laptop_dealers


def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Dealer Name', 'Dealer Link'])
        writer.writerows(data)


if __name__ == '__main__':
    file_path = 'downloaded_pages/techasoft.html'
    
    with open(file_path, 'r') as file:
        html_content = file.read()
    
    dealers_data = extract_bulk_laptop_dealers(html_content)
    save_to_csv(dealers_data)