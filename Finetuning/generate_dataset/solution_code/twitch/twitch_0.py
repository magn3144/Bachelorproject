import csv
from urllib.parse import urlparse
from lxml import etree

# Load HTML file
html_file = 'downloaded_pages/twitch.html'
with open(html_file, 'r') as file:
    html_data = file.read()

# Extract username and follower count using XPath
tree = etree.HTML(html_data)
usernames = tree.xpath('//div[@class="username"]/text()')
follower_counts = tree.xpath('//div[@class="follower-count"]/text()')

# Create a list of scraped data
data = list(zip(usernames, follower_counts))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'Follower Count'])
    writer.writerows(data)