import csv
from lxml import html

# Open the HTML file
with open('downloaded_pages/techasoft.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find all the artificial intelligence services
ai_services = tree.xpath('//a[contains(text(), "Artificial Intelligence")]')

# Extract the names and links
names = [service.text_content() for service in ai_services]
links = [service.get("href") for service in ai_services]

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Link'])
    writer.writerows(zip(names, links))