import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/twitter.html', 'r') as file:
    html_content = file.read()

# Create an ElementTree object from the HTML content
tree = html.fromstring(html_content)

# Find the target element using XPath
target_element = tree.xpath("/html/body/noscript/div/p[3]/a[5]")[0]

# Extract the text from the target element
scraped_data = target_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([scraped_data])