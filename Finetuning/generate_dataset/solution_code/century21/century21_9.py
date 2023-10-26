import csv
from lxml import etree

# Define the XPath for the "arrow" title tag
arrow_xpath = '/html/body/div[1]/div[3]/div[2]/div[1]/footer/div[2]/div/div[1]/div[1]/div/svg/title'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse('downloaded_pages/century21.html', parser)

# Find the "arrow" title tag using XPath
arrow_title = tree.xpath(arrow_xpath)[0].text

# Create a CSV file and write the scraped data
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title'])
    writer.writerow([arrow_title])