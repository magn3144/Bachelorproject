import csv
from lxml import etree

# Define the target HTML file path
html_file_path = 'downloaded_pages/4chan.html'

# Define the XPath expressions for the Janitor acceptance emails
janitor_email_xpath = "//h4[contains(text(),'Janitor acceptance emails')]"

# Parse the HTML file
tree = etree.parse(html_file_path)

# Find all elements matching the Janitor acceptance email XPath
janitor_email_elements = tree.xpath(janitor_email_xpath)

# Extract the text and XPath of the Janitor acceptance emails
scraped_data = []
for element in janitor_email_elements:
    email_text = element.text.strip()
    email_xpath = tree.getpath(element)
    scraped_data.append([email_text, email_xpath])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Email', 'XPath'])
    writer.writerows(scraped_data)