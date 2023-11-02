import csv
from lxml import etree

# Define the file path to the HTML file
path = "downloaded_pages/usajobs.html"

# Define the category
category = "Jobs"

# Define the XPaths for the desired information
city_xpath = "/html/body/section/section/div/aside/div/div[2]/div[3]/div[2]/ul/li[1]/div/div[2]/ul/li[1]/div/ul/li/p"

# Parse the HTML file using lxml
parser = etree.HTMLParser()
tree = etree.parse(path, parser)

# Find all the cities using the XPath
cities = tree.xpath(city_xpath)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'City'])
    for city in cities:
        writer.writerow([category, city.text.strip()])