
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the XPath for the element containing the DTU adress
address_xpath = '//*[@id="footerJob"]/div/p/a'

# Find the element using the XPath
address_element = tree.xpath(address_xpath)[0]

# Get the text from the element
address_text = address_element.text

# Remove quotation marks from the address text
address_text = address_text.replace('"', '')

# Add quotation marks around the address text
address_text = '"' + address_text + '"'

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([address_text])
