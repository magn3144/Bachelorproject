import csv
from lxml import html

# Define the XPath expressions for the review bodies
xpaths = [
    "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[4]/a/div[3]/div/div/p[2]",
    "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[6]/a/div[3]/div/div/p[2]",
    "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[7]/a/div[3]/div/div/p[2]",
]

# Load the HTML file
with open('downloaded_pages/trustpilot.html', 'r') as f:
    html_content = f.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract the review bodies using the XPath expressions
review_bodies = []
for xpath in xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        review_bodies.append(element.text.strip())

# Save the review bodies as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Review Body'])
    for body in review_bodies:
        writer.writerow([body])