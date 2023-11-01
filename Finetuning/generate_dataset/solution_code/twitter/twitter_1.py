import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/twitter.html', 'r') as f:
    html_content = f.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the target paragraph element using XPath
target_element = soup.find('p', xpath='/html/body/noscript/div/p[1]')

# Get the text from the target element
text = target_element.text.strip()

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([text])