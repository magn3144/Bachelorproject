import csv
from lxml import etree

# Paths to HTML elements
h1_xpath = "/html/body/noscript/div/h1"
p1_xpath = "/html/body/noscript/div/p[1]"
a_xpath = "/html/body/noscript/div/p[2]/a"
p2_a_xpath = "/html/body/noscript/div/p[3]/a[5]"
data = []

# Read the HTML file
with open("downloaded_pages/twitter.html", "r", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Scrape the text from the a tag
a_element = tree.xpath(a_xpath)
if len(a_element) > 0:
    data.append(a_element[0].text)

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(data)