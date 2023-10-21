import csv
from bs4 import BeautifulSoup

# Define the path to the HTML file
html_file = 'downloaded_pages/reddit.html'

# Open the HTML file and create a BeautifulSoup object
with open(html_file, 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find all the elements containing the author's username and the date of the post
author_elements = soup.find_all('a', class_='wM6scouPXXsFDSZmZPHRo DjcdNGtVXPcxG0yiFXIoZ _23wugcdiaj44hdfugIAlnX')
date_elements = soup.find_all('a', class_='_3yx4Dn0W3Yunucf5sVJeFU')

# Extract the text from the elements
authors = [element.get_text() for element in author_elements]
dates = [element.get_text() for element in date_elements]

# Define the path to save the CSV file
csv_file = 'scraped_data.csv'

# Write the scraped data to the CSV file
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Author', 'Date'])
    writer.writerows(zip(authors, dates))
