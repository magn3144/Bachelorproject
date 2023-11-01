import csv
from urllib.parse import urlparse
from lxml import etree

# Define the HTML elements and their corresponding XPaths
html_elements = [
    {
        "element": "a",
        "xpath": "/html/body/div[1]/div[4]/div/div/div[2]/a"
    },
    {
        "element": "a",
        "xpath": "/html/body/div[1]/div[3]/div/div/div[2]/a"
    },
    # Add other sign-in link elements here
]

# Read the HTML file
with open("downloaded_pages/artstation.html", "r", encoding="utf-8") as file:
    html_data = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.parse(html_data, parser)

# Extract the sign-in links
links = []
for element in html_elements:
    elements = tree.xpath(element["xpath"])
    for elem in elements:
        link = elem.get("href")
        if link:
            links.append(link)

# Extract the domain name from the URL
domain = urlparse("https://www.artstation.com").netloc

# Build the CSV file
csv_data = [["URL"]]
for link in links:
    if link.startswith("/"):
        url = f"https://{domain}{link}"
    else:
        url = link
    csv_data.append([url])

# Save the CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)