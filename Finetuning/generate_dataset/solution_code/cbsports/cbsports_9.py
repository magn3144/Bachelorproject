import csv
from lxml import html

# Define the target HTML file path
html_file_path = 'downloaded_pages/cbsports.html'

# Define the XPath for the paragraphs with a certain class
paragraph_xpath = "//p[@class='h4']"

# Parse the HTML file
with open(html_file_path, 'r') as file:
    html_content = file.read()
tree = html.fromstring(html_content)

# Extract the text from the paragraphs
paragraphs = tree.xpath(paragraph_xpath)
paragraph_texts = [paragraph.text_content().strip() for paragraph in paragraphs]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Text"])
    writer.writerows(zip(paragraph_texts))