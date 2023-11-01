import csv
from lxml import etree

# Define the XPaths for the target elements
section_header_xpath = "/html/body/div[1]/div[2]/div[1]/section[3]/div/h2"

# Open the HTML file and parse it with lxml
with open('downloaded_pages/myspace.html', 'rb') as f:
    html = f.read()
tree = etree.HTML(html)

# Extract the text from the section header element
section_header_element = tree.xpath(section_header_xpath)[0]
section_header_text = section_header_element.text.strip()

# Save the extracted data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Section Header'])
    writer.writerow([section_header_text])