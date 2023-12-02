
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the social links
social_links = tree.xpath('//div[@class="footer-social-icons"]/a')

# Extract the social links and their corresponding labels
social_links_and_labels = [(link.text, link.attrib['href']) for link in social_links]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Label', 'URL'])
    writer.writerows(social_links_and_labels)
