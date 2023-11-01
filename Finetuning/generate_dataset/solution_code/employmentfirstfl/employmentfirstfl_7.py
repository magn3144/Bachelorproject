import csv
from lxml import html

# Function to extract text from the specified XPath
def extract_text(tree, xpath):
    elements = tree.xpath(xpath)
    if elements:
        return elements[0].text_content().strip()
    else:
        return ""

# Open the HTML file and parse it using lxml
with open('downloaded_pages/employmentfirstfl.html', 'r') as f:
    html_content = f.read()
    tree = html.fromstring(html_content)

# Extract text from the screen-reader-text span using the specified XPath
text_xpath = "/html/body/div/a[@class='skip-link screen-reader-text']"
text = extract_text(tree, text_xpath)

# Write the extracted text to a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Text'])
    writer.writerow([text])