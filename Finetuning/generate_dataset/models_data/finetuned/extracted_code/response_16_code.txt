
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find all the elements with the class "t1jojoys"
elements = tree.xpath("//div[@class='t1jojoys']")

# Create a list to store the scraped data
scraped_data = []

# Loop over the elements
for element in elements:
    # Get the title of the element
    title = element.get('id')

    # Get the text of the element
    text = element.text

    # Add the data to the list
    scraped_data.append((title, text))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Text'])
    writer.writerows(scraped_data)
