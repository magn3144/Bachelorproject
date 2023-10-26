import os
import csv
from lxml import etree

# Define path to the HTML file
html_file = "downloaded_pages/nytimes.html"

# Define XPaths of the navigation sections
xpaths = [
    "/html/body/div/div[2]/nav/div/div[2]/div/section[1]/h3",
    "/html/body/div/div[2]/nav/div/div[2]/div/section[3]/h3",
    "/html/body/div/div[2]/nav/div/div[2]/div/section[4]/h3",
    "/html/body/div/div[2]/nav/div/div[2]/div/section[5]/h3",
]

# Create CSV file for saving scraped data
csv_file = "scraped_data.csv"

# Scrape the labels of the navigation sections
labels = []
try:
    # Parse the HTML file
    tree = etree.parse(html_file, etree.HTMLParser())

    # Get the labels using XPaths
    for xpath in xpaths:
        label = tree.xpath(xpath)
        if label:
            labels.append(label[0].text)
        else:
            labels.append("N/A")
except Exception:
    pass

# Save the scraped data as a CSV file
try:
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Navigation Section Labels"])
        writer.writerows(zip(labels))

    print(f"Scraped data saved successfully as '{csv_file}'")
except Exception as e:
    print(f"Error saving scraped data: {e}")