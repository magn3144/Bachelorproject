
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find the newsletter heading
newsletter_heading = tree.xpath('//h2[contains(text(), "Newsletter")]')[0]

# Extract the text from the newsletter heading
newsletter_text = newsletter_heading.text_content().strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([newsletter_text])
