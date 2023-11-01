import csv
from lxml import etree

# Define the target HTML file path
html_file = "downloaded_pages/top.html"

# Define the XPath of the <h2> element
h2_xpath = "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/button[1]/div/div[1]/h2"

# Parse the HTML file
tree = etree.parse(html_file)

# Find the <h2> element using the XPath
h2_element = tree.xpath(h2_xpath)[0]

# Get the text from the <h2> element
h2_text = h2_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Scraped Data'])
    writer.writerow([h2_text])