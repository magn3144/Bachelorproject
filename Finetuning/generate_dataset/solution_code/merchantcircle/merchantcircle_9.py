import csv
from lxml import html

# Open and parse the HTML file
with open('downloaded_pages/merchantcircle.html', 'r') as f:
    page_content = f.read()
tree = html.fromstring(page_content)

# Find all the organizations mentioned on the webpage
organizations = tree.xpath("//a[contains(@class, 'url')]")
data = []

# Extract the names and URLs of the organizations
for org in organizations:
    name = org.text.strip()
    url = org.get('href', '')
    data.append([name, url])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'URL'])
    writer.writerows(data)