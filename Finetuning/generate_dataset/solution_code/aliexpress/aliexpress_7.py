import csv
from lxml import etree

# Define the XPath for the "Help" section
help_xpath = '/html/body/div[7]/div/div[1]/div[1]/dl/dd'

# Open the HTML file
with open('downloaded_pages/aliexpress.html', 'r') as file:
    # Parse the HTML content
    tree = etree.parse(file)

    # Find the "Help" section
    help_section = tree.xpath(help_xpath)

    # Extract the text from the "Help" section
    help_text = help_section[0].text.strip()

    # Create a list with the extracted text
    data = [help_text]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Help'])
    writer.writerow(data)