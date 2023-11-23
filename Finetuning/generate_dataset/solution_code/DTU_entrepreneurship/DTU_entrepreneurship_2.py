from lxml import html
import csv

tree = html.parse('downloaded_pages/DTU_entrepreneurship.html')
address_object = tree.xpath('//*[@id="footerAbout"]/div[2]/div[2]/p[1]')
# Get first three lines of text in the element
address = address_object[0].text_content().split('\n')[:3]
# Concatenate the lines to a single string
address = ' '.join(address)
# Remove commas
# address = address.replace(',', '')
# Remove quotation marks in address string
address = address.replace('"', '')
# Add quotation marks around the address string
# address = '"' + address + '"'

with open('scraped_data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([address])