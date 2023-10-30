import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/bloggersroad.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all "Continue reading" links and their XPaths
links = soup.find_all('a', class_='more-link')

# Extract the href attribute and XPath for each link
data = []
for link in links:
    href = link.get('href')
    xpath = link.xpath('ancestor-or-self::node()[not(self::text() or self::comment())]/preceding::node()/count(preceding-sibling::*) + 1')
    data.append([href, xpath])

# Save the data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Link', 'XPath'])
    writer.writerows(data)