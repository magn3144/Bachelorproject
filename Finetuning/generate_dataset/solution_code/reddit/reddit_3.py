import csv
from lxml import etree

# Define the HTML elements with their corresponding XPaths
html_elements = {
    "privacy_policy_span": {
        "xpath": "/html/body/div[1]/div/div[2]/div[3]/div/section/div/section[1]/div/span[3]/a[2]",
        "text": ""
    }
}

# Parse the HTML file
html_path = "downloaded_pages/reddit.html"
with open(html_path, "r") as file:
    html_content = file.read()

html_tree = etree.HTML(html_content)

# Extract the information from the HTML elements
for element_name, element_info in html_elements.items():
    xpath = element_info["xpath"]
    element = html_tree.xpath(xpath)

    if element:
        element_text = element[0].text
        element_info["text"] = element_text

# Save the scraped data as a CSV file
csv_path = "scraped_data.csv"
with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    
    for element_name, element_info in html_elements.items():
        writer.writerow([element_name, element_info["text"]])