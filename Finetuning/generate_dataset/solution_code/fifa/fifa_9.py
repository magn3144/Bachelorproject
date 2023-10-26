import csv
from lxml import etree

# Define the target HTML file path
html_file_path = "downloaded_pages/fifa.html"

# Define the XPaths of the relevant elements
xpaths = [
    ("/html/body/div/div/main/div/section[6]/div/div[1]/div/div[1]/h2/span[1]/span", "tournament_highlights"),
    ("/html/body/div/div/main/div/section[6]/div/div[1]/div/div[1]/h2/span[2]/span", "tournament_highlights"),
]

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file_path, parser)

# Extract the values using the XPaths
results = []
for xpath, label in xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        result = {"label": label, "description": element.text}
        results.append(result)

# Save the results to a CSV file
filename = "scraped_data.csv"
with open(filename, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["label", "description"])
    writer.writeheader()
    writer.writerows(results)