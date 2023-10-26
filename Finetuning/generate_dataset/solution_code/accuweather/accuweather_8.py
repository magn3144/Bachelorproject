import csv
import re

from lxml import html

# Define the target HTML file path
html_file = "downloaded_pages/accuweather.html"

# Define the XPath for the current air quality information
air_quality_xpath = '/html/body/div/div[7]/div[1]/div[1]/div[1]/div/div[3]/div[2]'

# Load the HTML file
with open(html_file, "r") as file:
    page_content = file.read()

# Create an HTML tree from the page content
tree = html.fromstring(page_content)

# Scrape the current air quality information using the XPath
air_quality_element = tree.xpath(air_quality_xpath)[0]

# Extract the text and clean it
air_quality_text = air_quality_element.text_content().strip()

# Remove excess whitespaces and newline characters
air_quality_text = re.sub('\s+', ' ', air_quality_text)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Task', 'Air Quality'])
    writer.writerow(['Weather Websites', 'Scrape the current air quality information', air_quality_text])