import csv
from lxml import etree

# Load the HTML file
html_path = 'downloaded_pages/urbandictionary.html'
parser = etree.HTMLParser()
tree = etree.parse(html_path, parser)

# Get the "Advertise" link using its XPath
advertise_link_xpath = '/html/body/div/header/div[2]/div[1]/div/div/ul/li[5]/a'
advertise_link_element = tree.xpath(advertise_link_xpath)[0]
advertise_link_text = advertise_link_element.text

# Save the scraped data as a CSV file
csv_path = 'scraped_data.csv'
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link Text', 'XPath'])
    writer.writerow([advertise_link_text, advertise_link_xpath])