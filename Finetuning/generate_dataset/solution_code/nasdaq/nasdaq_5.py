import csv
from lxml import etree

# Load the HTML file
parser = etree.HTMLParser()
tree = etree.parse('downloaded_pages/nasdaq.html', parser)

# Define the XPath expressions for header elements
h1_xpath = '/html/body/div[2]/div/main/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/h1'
h2_xpath = '/html/body/div[7]/div[2]/div/div/div[2]/h2'
h3_xpath = '/html/body/div[2]/div/main/div[2]/div[2]/div[2]/aside/*[starts-with(name(), "h3")]'

# Scrape the header data
h1_text = tree.xpath(h1_xpath)[0].text.strip() if tree.xpath(h1_xpath) else ''
h2_text = tree.xpath(h2_xpath)[0].text.strip() if tree.xpath(h2_xpath) else ''
h3_data = [elem.text.strip() for elem in tree.xpath(h3_xpath)]

# Prepare the scraped data as a list of dictionaries
scraped_data = []
scraped_data.append({'Header 1': h1_text, 'Header 2': h2_text, 'Header 3': h3_data})

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Header 1', 'Header 2', 'Header 3']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)