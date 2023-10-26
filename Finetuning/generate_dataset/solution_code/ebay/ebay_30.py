import csv
from lxml import etree

# Define the target HTML file path
html_file = "downloaded_pages/ebay.html"

# Define the XPath for the element containing the text for "Announcements"
announcements_xpath = "/html/body/div[6]/footer/div[2]/table/tbody/tr[1]/td/ul/li[2]/a"

# Parse the HTML file
tree = etree.parse(html_file)
root = tree.getroot()

# Find the element containing the text for "Announcements"
announcements_element = root.xpath(announcements_xpath)[0]

# Extract the text for "Announcements"
announcements_text = announcements_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Task', 'Text'])
    writer.writerow(['E-commerce', 'Announcements', announcements_text])