import csv
from lxml import html

# Open the HTML file
with open('downloaded_pages/google news.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Parse the HTML content
doc = html.fromstring(content)

# Find all <span> tags with class "iDvCIf xfudi"
span_elements = doc.xpath('//span[@class="iDvCIf xfudi"]')

# Extract the text and corresponding XPaths
data = []
for span in span_elements:
    text = span.text.strip()
    xpath = doc.getpath(span)
    data.append([text, xpath])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Text', 'XPath'])
    writer.writerows(data)