import csv
from lxml import html

# Local path to the HTML file
path = 'downloaded_pages/myspace.html'

# XPaths for the list of artists
artist_xpath = '/html/body/div[1]/div[2]/div[1]/section[1]/div[2]/article/div/div[1]/ul/li/a/div[2]/span[1]'

# Open the HTML file and parse it
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
tree = html.fromstring(content)

# Scrape the list of artists
artists = tree.xpath(artist_xpath)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Artist'])
    for artist in artists:
        writer.writerow([artist.text_content()])