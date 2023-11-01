from lxml import html
import csv

# Define the target HTML file path
html_file_path = 'downloaded_pages/dst.html'

# Load the HTML file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Define the XPath for the source data
source_data_xpath = '/html/body/div[1]/main/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[3]/div/div[5]'

# Get the source data element
source_data_element = tree.xpath(source_data_xpath)[0]

# Get the source data text
source_data = source_data_element.text.strip()

# Save the source data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Source Data'])
    writer.writerow([source_data])