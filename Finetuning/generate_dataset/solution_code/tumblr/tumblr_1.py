import csv
from lxml import etree

# Locating the HTML file
html_file = 'downloaded_pages/tumblr.html'

# Reading the HTML file and parsing it
with open(html_file, 'r') as file:
    html = file.read()
    
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Extracting all usernames from the posts
username_elements = tree.xpath('//div[contains(@class, "rZlUD") or contains(@class, "HPjtV")]')

usernames = [element.text.strip() for element in username_elements]

# Saving the scraped data to a CSV file
csv_file = 'scraped_data.csv'

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Username'])
    writer.writerows([[username] for username in usernames])