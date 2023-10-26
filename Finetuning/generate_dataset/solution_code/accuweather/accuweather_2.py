import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/accuweather.html', 'r') as f:
    html = f.read()

# Parse the HTML
tree = etree.HTML(html)

# Define the XPath for the element containing the current weather condition
xpath = '/html/body/div/div[7]/div[1]/div[1]/a[1]/div[2]/span[@class="phrase"]'

# Find the element using the XPath
element = tree.xpath(xpath)[0]

# Get the text of the element
current_weather = element.text

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Current Weather'])
    writer.writerow([current_weather])