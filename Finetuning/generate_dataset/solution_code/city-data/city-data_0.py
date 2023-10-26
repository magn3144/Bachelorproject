import csv
from lxml import html

# Define the target HTML file path
html_file_path = 'downloaded_pages/city-data.html'

# Define the XPath expression for the target element
target_xpath = '/html/body/div[3]/div[4]/h1/span'

# Parse the HTML file
tree = html.parse(html_file_path)

# Find the target element using XPath
target_element = tree.xpath(target_xpath)[0]

# Extract the text from the target element
extracted_text = target_element.text

# Save the extracted text as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([extracted_text])