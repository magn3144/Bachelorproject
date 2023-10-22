import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/washingtonpost.html'

# Open the HTML file and create a BeautifulSoup object
with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all the labels on the page
labels = soup.find_all('label')

# Extract the text from the labels
label_texts = [label.text.strip() for label in labels]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Labels'])
    writer.writerows(zip(label_texts))
