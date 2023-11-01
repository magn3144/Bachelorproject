import csv
import os
from lxml import etree

# Function to extract the names of the sculptures from the given HTML elements
def get_sculpture_names(elements):
    sculpture_names = []
    for element in elements:
        if "sculptures" in element.text:
            sculpture_name = element.text.split(" ")[0]
            sculpture_names.append(sculpture_name)
    return sculpture_names

# Define the local path to the HTML file
html_file_path = "downloaded_pages/wikipedia.html"

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file_path, parser)

# Get the HTML elements using their XPaths
elements = tree.xpath("//a[contains(., 'sculptures')]/preceding-sibling::b/a")

# Get the names of the sculptures
sculpture_names = get_sculpture_names(elements)

# Save the sculpture names as a CSV file
csv_file_path = "scraped_data.csv"
with open(csv_file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Sculpture Name"])
    writer.writerows([[name] for name in sculpture_names])

# Print a success message
print("Scraping and saving of sculpture names successful!")