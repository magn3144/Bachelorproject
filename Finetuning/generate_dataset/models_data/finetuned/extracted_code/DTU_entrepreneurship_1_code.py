
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all the social links
social_links = tree.xpath('//a[contains(@class, "sitelink")]')

# Extract the social links and their corresponding text
social_links_and_text = [(link.text, link.attrib['href']) for link in social_links]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Text', 'URL'])
    writer.writerows(social_links_and_text)
