import csv
from lxml import html

# Define the target file path and category
file_path = 'downloaded_pages/google news.html'
category = 'News'

# Define the XPath for the span tags with class "VfPpkd-StrnGf-rymPhb-b9t22c"
xpath = '//span[@class="VfPpkd-StrnGf-rymPhb-b9t22c"]'

# Parse the HTML file
with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()
tree = html.fromstring(html_content)

# Extract the text and corresponding XPaths
elements = tree.xpath(xpath)
data = [(element.text_content(), tree.getpath(element)) for element in elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Text', 'XPath'])
    writer.writerows(data)