import csv
from lxml import etree

def extract_text(element):
    if element is not None:
        return element.text.strip()
    return ""

# Load the HTML from the file
with open("downloaded_pages/fbi.html", "r") as file:
    html = file.read()

# Create an lxml tree from the HTML
tree = etree.HTML(html)

# Fetch the total number of results
results_element = tree.xpath("//p[contains(@class, 'right')]")
result_count = extract_text(results_element[0]) if len(results_element) > 0 else "Unknown"

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Task", "Result"])
    writer.writerow(["Government and Public Databases", "Total Number of Results", result_count])