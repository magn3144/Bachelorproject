import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/fbi.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find all the Crime Against Children links
links = tree.xpath("//a[contains(text(), 'Crimes Against Children')]")

# Extract the names and links
data = []
for link in links:
    name = link.text
    url = link.attrib['href']
    data.append((name, url))

# Save the data to CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Link'])
    writer.writerows(data)