import csv
import requests
from lxml import html

# Define the URL and XPath
url = "file:///downloaded_pages/9gag.html"
xpath = "/html/body/span"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
tree = html.fromstring(response.content)

# Extract the text from the hidden span element
hidden_span_text = tree.xpath(xpath)[0].text

# Split the text by comma to get individual URLs
urls = hidden_span_text.split(',')

# Write the scraped URLs to a CSV file
with open('scraped_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['URL'])
    for url in urls:
        writer.writerow([url])