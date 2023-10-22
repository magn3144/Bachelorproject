import csv
from bs4 import BeautifulSoup

# Open the HTML file and create a BeautifulSoup object
with open('downloaded_pages/espn.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all the headline elements
headlines = soup.find_all(['h1', 'h2', 'h3'])

# Extract the headline text and save them in a list
headline_texts = [headline.get_text() for headline in headlines]

# Write the headline data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline'])
    writer.writerows(zip(headline_texts))