import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/merchantcircle.html'
category = 'Directories'
data_elements = [
    '<a class="bottomSignature"> -- Latest Update February 04, 2011 at 06:10 AM by</a>',
    '<a id="_bl_link">A Buyerlink </a> inc. company. All Rights Reserved.'
    # Add more elements here if needed
]

# Scrape the text of all bottomSignature links
soup = BeautifulSoup(open(html_file), 'html.parser')
bottom_signature_links = soup.find_all('a', class_='bottomSignature')

# Extract the text and save as CSV
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category', 'Link Text'])

    for link in bottom_signature_links:
        writer.writerow([category, link.get_text().strip()])