import csv
from lxml import etree

# Define the target page's information
category = "Social Media"
local_path = "downloaded_pages/4chan.html"

# Define a function to retrieve option labels and their XPaths from the target page
def retrieve_option_labels_and_xpaths():
    option_labels_xpaths = []
    with open(local_path, "r") as file:
        content = file.read()
        parser = etree.HTMLParser()
        tree = etree.fromstring(content, parser)
        
        # Find all option elements
        option_elements = tree.xpath("//option")
        
        # Retrieve option labels and their XPaths
        for option in option_elements:
            label = option.text.strip()
            xpath = tree.getpath(option)
            option_labels_xpaths.append([label, xpath])
    
    return option_labels_xpaths

# Retrieve option labels and their XPaths from the target page
option_labels_xpaths = retrieve_option_labels_and_xpaths()

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Option Label", "XPath"])
    writer.writerows(option_labels_xpaths)