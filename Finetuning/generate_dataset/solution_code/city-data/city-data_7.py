import csv
from lxml import html

# Open the HTML file
with open('downloaded_pages/city-data.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract the text from the <p> element using XPath
text_elements = tree.xpath('/html/body/div[3]/div[4]/p[1]')
text = text_elements[0].text.strip() if text_elements else ''

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Text'])
    writer.writerow([text])