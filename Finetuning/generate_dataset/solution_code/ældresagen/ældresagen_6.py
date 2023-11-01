import csv
from lxml import etree

# Parse the HTML file
html_file = "downloaded_pages/ældresagen.html"
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Define the XPath for the text about the need to move
xpath = "/html/body/div[2]/main/section[1]/section[2]/article/header/div/p"

# Find the element using the XPath
element = tree.xpath(xpath)

# Extract the text from the element
text = element[0].text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['text_about_need_to_move'])
  writer.writerow([text])