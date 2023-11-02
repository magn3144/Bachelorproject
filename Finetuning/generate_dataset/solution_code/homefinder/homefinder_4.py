import csv
from lxml import etree

def scrape_html(html_file, xpath):
    with open(html_file, 'r') as file:
        tree = etree.parse(file)
        elements = tree.xpath(xpath)
        return [element.text.strip() for element in elements]

# Define the HTML file path and XPath for the "Sign In" button
html_file = 'downloaded_pages/homefinder.html'
xpath = '/html/body/div/div/div/header/nav/div/div[2]/div/ul[1]/li/button/span[2]'

# Scrape the text of the "Sign In" button
sign_in_text = scrape_html(html_file, xpath)[0]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Sign In'])
    writer.writerow([sign_in_text])