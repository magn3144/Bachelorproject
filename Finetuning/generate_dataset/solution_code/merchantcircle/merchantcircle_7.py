import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/merchantcircle.html'
target_elements = ['viewMoreLink']

# Scrape the text of all the viewMoreLink links
scraped_data = []
with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    for element in target_elements:
        links = soup.find_all('a', class_=element)
        for link in links:
            scraped_data.append(link.get_text())

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(scraped_data)