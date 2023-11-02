import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/stackexchange-hot-questions.html', 'r') as file:
    html_content = file.read()

# Create an ElementTree object from the HTML content
tree = etree.HTML(html_content)

# Find the "All Sites" section
all_sites_section = tree.xpath('/html/body/div/header[2]/div/ul/li[1]/a')

# Get the names and URLs of the sites
site_names = [site.text for site in all_sites_section]
site_urls = [site.get('href') for site in all_sites_section]

# Store the data in a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'URL'])
    writer.writerows(zip(site_names, site_urls))