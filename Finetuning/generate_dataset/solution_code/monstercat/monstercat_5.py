import csv
from lxml import html

# Define the target HTML file path
html_file_path = "downloaded_pages/monstercat.html"

# Define the XPaths for the forums and review sites
forums_xpath = "/html/body/div[4]/div[4]/div[2]/header/div/div[2]/div[2]/div/div/div/ul/li[2]/div/div/ul/li/div/ul/li/a"
review_sites_xpath = "/html/body/div[4]/div[4]/div[2]/header/div/div[2]/div[2]/div/div/div/ul/li[2]/div/div/ul/li/div/ul/li[2]/a"

# Read the HTML file and create an lxml etree
with open(html_file_path, "r") as file:
    html_content = file.read()
tree = html.fromstring(html_content)

# Scrape the list of forums
forums = tree.xpath(forums_xpath)
forum_data = [(forum.text, forum.get("href")) for forum in forums]

# Scrape the list of review sites
review_sites = tree.xpath(review_sites_xpath)
review_site_data = [(site.text, site.get("href")) for site in review_sites]

# Combine the forum and review site data
scraped_data = forum_data + review_site_data

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "URL"])
    writer.writerows(scraped_data)