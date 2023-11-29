import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the newsletter heading
newsletter_heading = tree.xpath('//h2[contains(text(), "Newsletter")]')

# Extract the text from the heading
newsletter_text = newsletter_heading[0].text.strip()

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([newsletter_text])
