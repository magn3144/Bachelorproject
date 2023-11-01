import csv
from lxml import html

# Define the XPath for the "Discover" section header
discover_xpath = "/html/body/div[1]/section/div[1]/h2"

# Read the HTML file
with open("downloaded_pages/myspace.html", "r") as f:
    html_content = f.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract the text from the "Discover" section header
discover_header = tree.xpath(discover_xpath)[0].text

# Write the extracted data to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Discover Section Header'])
    writer.writerow([discover_header])