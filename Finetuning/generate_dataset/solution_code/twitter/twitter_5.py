import csv
from lxml import html

# Define the HTML file path
html_file = "downloaded_pages/twitter.html"

# Define the XPath for the span tag
span_xpath = "/html/body/div/div/div/div[2]/form/div/button/div/div/span/span"

# Load the HTML file
with open(html_file, "r") as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract the text from the span tag
span_text = tree.xpath(span_xpath)[0].text

# Write the scraped data to CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([span_text])