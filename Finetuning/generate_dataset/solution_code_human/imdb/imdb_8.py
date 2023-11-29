import csv
from lxml import html

# Open the file and parse into an html element tree
with open('downloaded_pages/imdb.html', 'r') as file:
    tree = html.fromstring(file.read())

# XPath to match all footer link elements
footer_link_elements = tree.xpath('//body//footer//a')

# Open CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Link Text', 'Link URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    # Write each footer link to the CSV
    for element in footer_link_elements:
        writer.writerow({ 'Link Text': element.text_content().strip(), 'Link URL': element.get('href') })