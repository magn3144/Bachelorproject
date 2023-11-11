import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/DTU-entrepreneurship.html', 'r') as file:
    html = file.read()

# Create an lxml element from the HTML
root = etree.HTML(html)

# Find the heading element using the XPath
heading_xpath = "/html/body/form/div[3]/footer/div[1]/div/div[2]/h2"
heading_element = root.xpath(heading_xpath)[0]

# Get the text from the heading element
heading_text = heading_element.text.strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Scraped Data'])
    writer.writerow(['Educational Websites', heading_text])