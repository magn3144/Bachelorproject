import csv
from lxml import html

# Define the XPaths for the follower count of each blog
follower_xpath = "/html/body/div/div/div[2]/div/div[2]/div/div[1]/main/div[3]/div[2]/div[position() > 1]/div/div/div/article/header/div[2]/div/div[2]/a/span"

# Load the HTML file
with open("downloaded_pages/tumblr.html", "r", encoding="utf-8") as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Scrape the follower count for each blog
follower_counts = tree.xpath(follower_xpath)

# Write the scraped data to CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Follower Count"])
    writer.writerows([[count] for count in follower_counts])