import csv
from lxml import etree

# Open the HTML file
with open("downloaded_pages/wikipedia.html", "r") as file:
    html_content = file.read()

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.fromstring(html_content, parser)

# Find all the tool names
tools = tree.xpath("//div[@class='vector-pinnable-header-label']/text()")

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tool Names'])
    for tool in tools:
        writer.writerow([tool])