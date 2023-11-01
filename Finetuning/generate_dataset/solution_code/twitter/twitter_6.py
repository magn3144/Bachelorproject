import csv
from lxml import etree

html_file = "downloaded_pages/twitter.html"
xpath = "/html/body/noscript/div/p[3]/a[3]"

# Parse the HTML file
tree = etree.parse(html_file)
root = tree.getroot()

# Find the desired element using XPath
element = root.xpath(xpath)[0]

# Get the text from the element
text = element.text

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Scraped Text'])
    writer.writerow(['Social Media', text])