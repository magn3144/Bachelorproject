import csv
from lxml import etree

# Define the XPath expressions for the desired elements
featured_artist_xpath = "//h4[@class='recentImage__details-title']"
song_xpath = "//a[contains(@href, '/wiki/') and not(contains(@class, 'new'))]"

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse("downloaded_pages/monstercat.html", parser)

# Find all the featured artists and their songs
featured_artists = tree.xpath(featured_artist_xpath)
songs = tree.xpath(song_xpath)

# Create a list of dictionaries with the scraped data
scraped_data = []
for artist, song in zip(featured_artists, songs):
    scraped_data.append({"Artist": artist.text, "Song": song.text})

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Artist", "Song"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)