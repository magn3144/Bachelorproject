import csv
from lxml import etree

# Define the XPaths for the elements to be scraped
title_xpath = "//h2[@class='movie-title']/a/text()"
rating_xpath = "//span[@class='movie-rating']/text()"

# Load the HTML file using the local path
html = etree.parse("downloaded_pages/twitch.html", etree.HTMLParser())

# Extract the titles and ratings using the XPaths
titles = html.xpath(title_xpath)
ratings = html.xpath(rating_xpath)

# Create a list of dictionaries for the scraped data
scraped_data = []
for title, rating in zip(titles, ratings):
    scraped_data.append({"Title": title, "Rating": rating})

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Title", "Rating"])
    writer.writeheader()
    writer.writerows(scraped_data)