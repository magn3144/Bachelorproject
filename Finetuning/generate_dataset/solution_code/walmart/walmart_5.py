import csv
import requests
from lxml import html

# Set the URL and local path
url = 'https://www.walmart.com'
local_path = 'downloaded_pages/walmart.html'

# Load the HTML file
with open(local_path, 'r') as file:
    html_content = file.read()

# Create an XPath selector
selector = html.fromstring(html_content)

# Find the meat and cheese alternatives prices
meat_cheese_elements = selector.xpath('//a[contains(@class, "f6 no-underline black db underline-hover pb2 mb1") and contains(text(), "Meat & Cheese Alternatives")]/@href')

if meat_cheese_elements:
    # Get the URL of the meat and cheese alternatives page
    meat_cheese_url = url + meat_cheese_elements[0]

    # Scrape the meat and cheese alternatives prices
    response = requests.get(meat_cheese_url)
    if response.status_code == 200:
        meat_cheese_html = response.text
        meat_cheese_selector = html.fromstring(meat_cheese_html)
        prices = meat_cheese_selector.xpath('//div[contains(@class, "gray mr1 f7 f6-l")]/text()')

        # Save the prices to a CSV file
        with open('scraped_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Price'])
            for price in prices:
                writer.writerow([price])
