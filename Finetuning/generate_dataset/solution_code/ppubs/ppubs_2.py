from bs4 import BeautifulSoup
import csv

# Open the HTML file
with open('downloaded_pages/ppubs.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all title and span tags
title_tags = soup.find_all('title')
span_tags = soup.find_all('span')

# Extract the text from tags
title_text = [tag.get_text(strip=True) for tag in title_tags]
span_text = [tag.get_text(strip=True) for tag in span_tags]

# Combine the texts
all_text = title_text + span_text

# Write the data to CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])
    writer.writerows([[text] for text in all_text])