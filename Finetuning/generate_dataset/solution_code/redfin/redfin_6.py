import csv
from lxml import html

# Define the path to the downloaded HTML file
html_file_path = "downloaded_pages/redfin.html"

# Parse the HTML file
with open(html_file_path, "r") as file:
    html_content = file.read()
tree = html.fromstring(html_content)

# Define the XPaths for h1, h2, h3 tags
h1_xpaths = [
    "/html/body/div[1]/div[8]/div[2]/div[2]/div[1]/div/div/div/h1"
]
h2_xpaths = [
    "/html/body/div[1]/div[8]/div[2]/div[7]/div/div[2]/h2",
    "/html/body/div[1]/div[8]/div[2]/div[7]/div/div[6]/h2"
]
h3_xpaths = [
    "/html/body/div[1]/div[8]/div[2]/div[7]/div/div[5]/h1",
    "/html/body/div[1]/div[8]/div[2]/div[7]/div/div[11]/div[2]/div[2]/div[1]/div/h3",
    "/html/body/div[1]/div[8]/div[2]/div[7]/div/div[1]/h3",
    "/html/body/div[1]/div[8]/div[2]/div[7]/div/div[4]/h2",
]

# Extract h1 tags and their XPaths
h1_tags = []
for xpath in h1_xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        h1_tags.append({
            'tag': element.tag,
            'xpath': xpath,
            'text': element.text_content().strip()
        })

# Extract h2 tags and their XPaths
h2_tags = []
for xpath in h2_xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        h2_tags.append({
            'tag': element.tag,
            'xpath': xpath,
            'text': element.text_content().strip()
        })

# Extract h3 tags and their XPaths
h3_tags = []
for xpath in h3_xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        h3_tags.append({
            'tag': element.tag,
            'xpath': xpath,
            'text': element.text_content().strip()
        })

# Combine all the tags
all_tags = h1_tags + h2_tags + h3_tags

# Save the scraped data as a CSV file
output_file = "scraped_data.csv"
with open(output_file, "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['tag', 'xpath', 'text'])
    writer.writeheader()
    writer.writerows(all_tags)