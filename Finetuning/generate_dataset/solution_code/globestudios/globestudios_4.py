import csv
from lxml import html

# Define the XPath expression for the "Longsleeve" element
longsleeve_xpath = "/html/body/div/div[2]/header/div/div/full-menu/ul/li[2]/div/ul/li[2]/ul/li[3]/a"

# Load the HTML file
with open('downloaded_pages/globestudios.html', 'r') as file:
    html_content = file.read()

# Create an ElementTree object from the HTML content
tree = html.fromstring(html_content)

# Find the desired element using the XPath expression
longsleeve_element = tree.xpath(longsleeve_xpath)[0]

# Extract the text from the element
longsleeve_text = longsleeve_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Longsleeve'])
    writer.writerow([longsleeve_text])