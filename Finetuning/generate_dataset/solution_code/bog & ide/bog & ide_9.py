import csv
from lxml import etree

# Define the XPath for the desired element
xpath = "/html/body/div/main/div[1]/div[2]/div/div[4]/div/div[1]/h4"

# Parse the HTML file
html = etree.parse("downloaded_pages/bog & ide.html", etree.HTMLParser())

# Find the element using XPath
element = html.xpath(xpath)
text = element[0].text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Heading Text'])
    writer.writerow([text])