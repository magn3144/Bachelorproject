import csv
from lxml import etree

def find_element_by_xpath(tree, xpath):
    return tree.xpath(xpath)[0].text

# Define the local path to the HTML file
html_file_path = "downloaded_pages/bog & ide.html"

# Define the XPath for the heading element
heading_xpath = "/html/body/div/main/div[1]/div[2]/div/section[1]/div[1]/h2"

# Read and parse the HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

tree = etree.HTML(html_content)

# Find the heading element by XPath
heading = find_element_by_xpath(tree, heading_xpath)

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Heading"])
    writer.writerow([heading])