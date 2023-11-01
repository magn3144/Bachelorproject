import csv
from pathlib import Path
from lxml import etree

# Define the HTML elements and their XPaths
elements = {
    "review_rating": "/html/body/div[1]/div/p",
    "review_comment": "/html/body/div[1]/div/p",
}

# Define the local path to the HTML file
html_file_path = 'downloaded_pages/quora.html'

# Parse the HTML file
html = etree.parse(html_file_path)

# Scraping the review ratings and comments
review_ratings = html.xpath(elements["review_rating"])
review_comments = html.xpath(elements["review_comment"])

# Combine the review ratings and comments into a list of tuples
data = list(zip(review_ratings, review_comments))

# Save the scraped data as a CSV file
output_file = "scraped_data.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Review Rating", "Review Comment"])
    writer.writerows(data)