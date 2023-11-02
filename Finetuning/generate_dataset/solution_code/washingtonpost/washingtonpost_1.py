import os
import csv
from bs4 import BeautifulSoup

# Read HTML file
file_path = 'downloaded_pages/washingtonpost.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extract dates and headlines
dates = soup.select('span.wpds-c-iKQyrV')
headlines = soup.select('h3.font-md.font-bold.font--headline')

# Prepare data for CSV
data = []
for date, headline in zip(dates, headlines):
    date_text = date.get_text(strip=True)
    headline_text = headline.get_text(strip=True)
    data.append([date_text, headline_text])

# Save data as CSV
output_path = 'scraped_data.csv'
with open(output_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Headline'])
    writer.writerows(data)