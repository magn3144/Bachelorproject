import csv
from lxml import etree

# Define the local path to the HTML file
file_path = "downloaded_pages/techasoft.html"

# Open the HTML file and parse it with lxml
with open(file_path, 'r') as file:
    html = file.read()
tree = etree.HTML(html)

# Find all the <a> elements that contain the text "HR and Payroll Management Software"
software_elements = tree.xpath("//a[contains(text(), 'HR and Payroll Management Software')]")

# Create a list to store the scraped data
data = []

# Iterate over the software elements and extract the names and links
for element in software_elements:
    name = element.text
    link = element.get("href")
    data.append({"Name": name, "Link": link})

# Save the scraped data as a CSV file
with open("scraped_data.csv", 'w', newline='') as csvfile:
    fieldnames = ["Name", "Link"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)