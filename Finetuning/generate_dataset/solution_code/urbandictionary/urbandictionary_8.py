import csv
from lxml import etree

# Define the HTML file path
html_file_path = "downloaded_pages/urbandictionary.html"

# Define the target element xpath
target_xpath = "/html/body/div/div/main/div/div[4]/section/div[3]/div/div[4]/a"

# Parse the HTML file
tree = etree.parse(html_file_path)

# Find the target element using the xpath
target_element = tree.xpath(target_xpath)[0]

# Extract the link text and its XPath
link_text = target_element.text
link_xpath = tree.getpath(target_element)

# Create a CSV file and write the scraped data
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Link Text", "Link XPath"])
    writer.writerow([link_text, link_xpath])