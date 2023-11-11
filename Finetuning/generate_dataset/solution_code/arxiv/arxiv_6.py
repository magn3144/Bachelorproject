import csv
from lxml import etree

# Load the HTML file
with open('downloaded_pages/arxiv.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Get the date and number of entries
date_xpath = '/html/body/div[4]/div/h3'
entries_xpath = '/html/body/div[4]/div/h3'

date_element = tree.xpath(date_xpath)[0]
entries_element = tree.xpath(entries_xpath)[0]

date = date_element.text.strip()
entries = entries_element.text.split()[3]

# Save the scraped data as CSV
data = [['Date', 'Number of Entries'], [date, entries]]

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)