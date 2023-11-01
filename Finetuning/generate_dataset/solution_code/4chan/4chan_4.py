import csv
from lxml import html

# Open the HTML file
with open('downloaded_pages/4chan.html', 'r') as file:
    content = file.read()

# Parse the HTML content
tree = html.fromstring(content)

# Find all thread subjects and their corresponding XPaths
subjects = tree.xpath("//td[contains(text(), 'Subject')]/following-sibling::td")
xpaths = tree.xpath("//td[contains(text(), 'Subject')]/following-sibling::td/@xpath")

# Create a list of dictionaries for the scraped data
data = []
for subject, xpath in zip(subjects, xpaths):
    data.append({
        'Subject': subject.text.strip(),
        'XPath': xpath
    })

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Subject', 'XPath'])
    writer.writeheader()
    writer.writerows(data)