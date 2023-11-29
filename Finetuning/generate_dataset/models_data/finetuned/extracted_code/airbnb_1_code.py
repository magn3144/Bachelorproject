
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find the sitemap link
sitemap_link = tree.xpath('//a[contains(text(), "Site")]')[0].get('href')

# Download the sitemap
with open('sitemap.html', 'w') as f:
    f.write(sitemap_link)

# Parse the sitemap
tree = html.fromstring(content)

# Find all the listings
listings = tree.xpath('//div[contains(@class, "t1jojoys")]')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'URL'])
    for listing in listings:
        title = listing.xpath('div[@class="t1jojoys dir dir-ltr"]')[0].text
        url = listing.xpath('a[@class="l1ovpqvx c1kblhex dir dir-ltr"]')[0].get('href')
        writer.writerow([title, url])
