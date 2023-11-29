import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the element with the text "11 NOVEMBER 2023"
element = tree.xpath("//div[contains(text(), '11 NOVEMBER 2023')]")

# Extract the text from the element
text = element[0].text.strip()

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([text])
