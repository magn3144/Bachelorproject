import csv
from lxml import html

# Open the HTML file and parse it using lxml
with open('downloaded_pages/ziprecruiter.html', 'r') as file:
    content = file.read()
    tree = html.fromstring(content)

# Find the 'Contact Us' section
contact_us_header = tree.xpath('//h3[contains(text(), "Contact Us")]')[0]
contact_us_items = []

# Get the sibling elements of the 'Contact Us' header
sibling = contact_us_header.getnext()
while sibling is not None and sibling.tag != 'h3':
    contact_us_items.append(sibling)
    sibling = sibling.getnext()

# Extract the email addresses from the contact us items
email_addresses = []
for item in contact_us_items:
    email = item.xpath('.//a[contains(@class, "email")]')
    if email:
        email_addresses.append(email[0].text_content())

# Save the scraped data in the CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Contact Us', 'Email Address'])
    for item, email in zip(contact_us_items, email_addresses):
        writer.writerow([item.text_content(), email])