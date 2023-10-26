import csv
from lxml import html

# Define the XPaths for the HTML elements to scrape
title_xpath = "/html/head/title"
link_xpath = "//a"
category_xpath = "//span[@id='sidebarPageRating']"

# Open the HTML file and parse it
with open("downloaded_pages/aboutus.html", "r", encoding="utf-8") as f:
    page_content = f.read()
tree = html.fromstring(page_content)

# Scrape the title
title = tree.xpath(title_xpath)[0].text if tree.xpath(title_xpath) else ""

# Scrape the links
links = [link.text for link in tree.xpath(link_xpath) if link.text]

# Scrape the category
category = tree.xpath(category_xpath)[0].text if tree.xpath(category_xpath) else ""

# Prepare the scraped data as a list of dictionaries
scraped_data = [{"Title": title, "Link": link, "Category": category} for link in links]

# Write the scraped data to a CSV file
with open("scraped_data.csv", "w", encoding="utf-8", newline="") as f:
    fieldnames = ["Title", "Link", "Category"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)