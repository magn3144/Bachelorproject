from bs4 import BeautifulSoup
import csv

html_file = 'downloaded_pages/merchantcircle.html'

with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    
review_links = soup.find_all('a', class_='review-link')

data = []
for link in review_links:
    data.append(link.get_text())

output_file = 'scraped_data.csv'
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)