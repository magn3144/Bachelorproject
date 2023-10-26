import csv
from lxml import etree

# Define the target page URL
page_url = "fbi"

# Define the local path to the HTML file
file_path = "downloaded_pages/fbi.html"

# Define the XPaths for the desired elements
names_xpath = "//a[@class='']"
links_xpath = "//a[@class='']/@href"

# Load the HTML file
with open(file_path, "r") as f:
    html_content = f.read()

# Create an element tree from the HTML content
tree = etree.HTML(html_content)

# Extract the names and links of the Ten Most Wanted Fugitives
names = tree.xpath(names_xpath)
links = tree.xpath(links_xpath)

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Link"])
    for name, link in zip(names, links):
        writer.writerow([name.text.strip(), link])