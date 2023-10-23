import csv
from lxml import html

# Define the XPaths for the target elements
title_xpath = "/html/head/title"
upvotes_xpath = "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[1]/div/div/div/div[3]/div[1]/div/h1"
# Add more XPaths for other data you may want to scrape

# Parse the HTML file
with open('downloaded_pages/reddit.html', 'r') as file:
    data = file.read()
tree = html.fromstring(data)

# Scrape the target data
title = tree.xpath(title_xpath)[0].text
upvotes = tree.xpath(upvotes_xpath)[0].text

# Save the scraped data as a CSV file
data = [[title, upvotes]]
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Upvotes'])
    writer.writerows(data)