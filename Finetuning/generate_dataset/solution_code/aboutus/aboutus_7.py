import csv
import lxml.html

# Open the HTML file
with open('downloaded_pages/aboutus.html', 'r') as file:
    html_data = file.read()

# Parse the HTML
tree = lxml.html.fromstring(html_data)

# Find all 'h3' and 'h4' elements
elements = tree.xpath('//h3 | //h4')

# Extract the texts
elements_text = [element.text_content() for element in elements]

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(elements_text)