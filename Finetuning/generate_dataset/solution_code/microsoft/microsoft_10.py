import csv
import requests
from lxml import etree

# Define the target URL and local path
url = "https://www.microsoft.com"
local_path = "downloaded_pages/microsoft.html"

# Download the HTML file
response = requests.get(url)
html = response.content

# Save the HTML file locally
with open(local_path, "wb") as file:
    file.write(html)

# Open the local HTML file for parsing
with open(local_path, "rb") as file:
    html_tree = etree.parse(file)

# Define the XPaths for the trending topics under the "Windows & enheder" category
xpaths = [
    '/html/body/div/section/div/div/div/div/article/div[1]/div/section/div/div/div[4]/h3',
    '/html/body/div/section/div/div/div/div/article/div[1]/div/section/div/div/div[3]/h3',
    '/html/body/div/section/div/div/div/div/article/div[1]/div/section/div/div/div[2]/ul/li[3]/p/a',
    '/html/body/div/section/div/div/div/div/article/div[1]/div/section/div/div/div[2]/h2',
    '/html/body/div/section/div/div/div/div/article/div[1]/div/section/h2'
]

# Scrape the names of the trending topics
trending_topics = []
for xpath in xpaths:
    elements = html_tree.xpath(xpath)
    for element in elements:
        trending_topics.append(element.text.strip())

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Trending Topic"])
    writer.writerows([[topic] for topic in trending_topics])