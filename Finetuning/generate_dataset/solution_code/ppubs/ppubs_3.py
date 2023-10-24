import csv
from lxml import etree

# Define the HTML file path
html_file = 'downloaded_pages/ppubs.html'

# Define the XPaths for table elements
table_xpath = '/html/body/div[2]/div/section[2]/div/div/div/div/div[2]/div/table'
header_xpath = '/thead/tr/th'
row_xpath = '/tbody/tr'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Extract table headers
headers = tree.xpath(table_xpath + header_xpath)
header_list = [header.text.strip() for header in headers]

# Extract table rows
rows = tree.xpath(table_xpath + row_xpath)

# Extract row data
data = []
for row in rows:
    row_data = [td.text.strip() for td in row.xpath('.//td')]
    data.append(row_data)

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header_list)
    writer.writerows(data)