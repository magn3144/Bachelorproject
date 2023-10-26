import csv
from lxml import html

# Read the local HTML file
with open('downloaded_pages/bbc_weather.html', 'r') as f:
    html_content = f.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find the accessibility help link using XPath
accessibility_help_link = tree.xpath('/html/body/div[9]/footer/div/div/div/ul/li[7]/a/text()')[0]

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Accessibility Help Link'])
    writer.writerow([accessibility_help_link])