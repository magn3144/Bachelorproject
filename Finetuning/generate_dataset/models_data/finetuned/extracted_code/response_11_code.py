
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the sitemap link
sitemap_link = tree.xpath('//a[contains(text(), "Site Map")]/@href')

# Download the sitemap
sitemap_url = 'https://airbnb.com' + sitemap_link[0]
sitemap_response = requests.get(sitemap_url)

# Parse the sitemap
sitemap_tree = html.fromstring(sitemap_response.content)

# Find all the URLs
urls = sitemap_tree.xpath('//*[@class="l1ovpqvx c1kblhex dir dir-ltr"]/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['URL'])
    writer.writerows([[url] for url in urls])
