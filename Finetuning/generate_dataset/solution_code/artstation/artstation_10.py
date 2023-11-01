import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/artstation.html', 'r') as file:
    content = file.read()

# Parse the HTML content
tree = html.fromstring(content)

# Find all sign-up links
signup_links = tree.xpath('//a[contains(text(), "Sign Up")]')

# Extract the URLs from the sign-up links
urls = [link.get('href') for link in signup_links]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['URL'])
    writer.writerows([[url] for url in urls])