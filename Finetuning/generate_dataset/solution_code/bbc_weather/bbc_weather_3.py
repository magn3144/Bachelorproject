import csv
from lxml import etree

# Define the HTML file path
html_file_path = 'downloaded_pages/bbc_weather.html'

# Define the XPaths for the weather span
weather_xpath = '/html/body/div[7]/header/div/div/nav[2]/ul/li[10]/a/span'

# Read the HTML file
with open(html_file_path, 'r') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find the weather span using XPath
weather_span = tree.xpath(weather_xpath)[0]

# Extract the weather text
weather_text = weather_span.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Weather'])
    writer.writerow([weather_text])