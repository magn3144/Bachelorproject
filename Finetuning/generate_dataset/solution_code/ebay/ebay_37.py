import csv
from lxml import etree

# Read the HTML file
html_file = 'downloaded_pages/ebay.html'
with open(html_file, 'r') as file:
    html_data = file.read()

# Parse HTML
tree = etree.HTML(html_data)

# Extract the text for "Vietnam"
result = tree.xpath('/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[1]/div/span/div/div[213]/span/text()')

# Write the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Scraped Text'])
    writer.writerow([result[0]])