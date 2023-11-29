
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find the elements with the given XPaths
elements = tree.xpath([
    "/html/body/form/div[3]/footer/div[1]/div/div[3]/div/div[2]/ul/li[2]/label",
    "/html/body/form/div[3]/footer/div[1]/div/div[3]/div/div[2]/ul/li[4]/label"
])

# Extract the text from the elements
text = [element.text for element in elements]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(text)
