from bs4 import BeautifulSoup
import csv

page_path = 'downloaded_pages/redfin.html'
csv_file = 'scraped_data.csv'

def get_agencies(html_file):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        agencies = soup.select('span.collapsedAddress.primaryLine')
        return [agency.get_text() for agency in agencies]

def save_to_csv(data, csv_file_name):
    with open(csv_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Agencies'])
        writer.writerows(data)

agencies = get_agencies(page_path)
save_to_csv(agencies, csv_file)