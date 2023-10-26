import csv
from lxml import etree

# Define the XPaths for the required section
verticalscope_xpath = "/html/body/div[1]/footer/div/div[1]/div[4]/div/ul/li"

# Load the HTML file
tree = etree.parse("downloaded_pages/avsforum.html")

# Find the VerticalScope Inc. section
verticalscope_element = tree.xpath(verticalscope_xpath)

# Extract the text from the section
verticalscope_text = verticalscope_element[0].text

# Write the extracted data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([verticalscope_text])