from lxml import etree
import csv

# Define the XPath for the country names in the footer
xpath_country_names = '//div[@class="country-selector_countryName__xJd6T"]/text()'

# Define the local path to the HTML file
local_path = 'downloaded_pages/trustpilot.html'

# Read the HTML file
with open(local_path, 'r') as f:
    html_content = f.read()

# Create an ElementTree object from the HTML content
tree = etree.HTML(html_content)

# Find all the country names using the XPath
country_names = tree.xpath(xpath_country_names)

# Save the country names as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Country'])
    writer.writerows(zip(country_names))