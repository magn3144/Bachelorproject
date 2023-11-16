import csv
from lxml import html

# Reading the HTML file
with open('downloaded_pages/DTU-entrepreneurship.html', 'r') as file:
    page_content = file.read()

# Parsing the HTML content
tree = html.fromstring(page_content)

# Extracting all labels
labels = tree.xpath('//label')

# Writing labels to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # insert each label's text in the csv file
    for label in labels:
        writer.writerow([label.text])