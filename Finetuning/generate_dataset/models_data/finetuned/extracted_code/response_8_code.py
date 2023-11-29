import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the paragraph with the text "All entrepreneurship and innovation courses are li"
paragraph = tree.xpath('//span[contains(text(), "All entrepreneurship and innovation courses are li")]/../parent::p')

# Extract the text from the paragraph
text = paragraph[0].text_content()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([text])
