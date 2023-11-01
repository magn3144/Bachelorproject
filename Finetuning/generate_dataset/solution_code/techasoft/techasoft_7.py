import csv
from lxml import etree

# Define the target page and its local path
target_page = 'techasoft'
local_path = 'downloaded_pages/techasoft.html'

# Define the XPath for the machine learning services
xpath = '/html/body/footer/div[1]/div/div[4]/ul[2]/li/a'

# Parse the HTML file
with open(local_path, 'r') as file:
    html_content = file.read()

html_tree = etree.HTML(html_content)

# Find all the machine learning services
services = html_tree.xpath(xpath)

# Extract the names and links of the machine learning services
service_names = [service.text for service in services]
service_links = [service.get('href') for service in services]

# Create a list of dictionaries containing the scraped data
scraped_data = []
for i in range(len(service_names)):
    scraped_data.append({'Name': service_names[i], 'Link': service_links[i]})

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Link']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)