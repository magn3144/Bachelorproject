import csv
from lxml import etree

# Define the XPath expressions for the article links
link_xpath = '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/li/div[3]/a[2]/h3'

# Read the HTML file
with open('downloaded_pages/bleacherreport.html', 'r') as f:
    html = f.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all the article links
links = tree.xpath(link_xpath)

# Extract the URLs from the links
urls = [link.get('href') for link in links]

# Save the URLs as a CSV file
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['URL'])
    for url in urls:
        writer.writerow([url])