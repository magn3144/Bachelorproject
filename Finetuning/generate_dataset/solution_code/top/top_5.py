import csv
from lxml import etree

# Define the XPath for the <h3> element
h3_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/article[3]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[3]/a[2]/span/span/div/div/p'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse('downloaded_pages/top.html', parser)

# Find the text from the <h3> element using the XPath
h3_element = tree.xpath(h3_xpath)
text = h3_element[0].text if h3_element else ''

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category', 'Scraped Text'])
    writer.writerow(['Digital Websites', text])