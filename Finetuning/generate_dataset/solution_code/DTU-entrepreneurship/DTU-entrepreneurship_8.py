import csv
from bs4 import BeautifulSoup

def get_contact_links(file_name):
    with open(file_name, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        contact_links = soup.findAll('a', text='Contact')
        
        with open('scraped_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Contact Links'])
            
            for link in contact_links:
                writer.writerow([link.get('href')])

get_contact_links('downloaded_pages/DTU-entrepreneurship.html')