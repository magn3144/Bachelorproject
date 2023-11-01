import csv
from lxml import etree

# Read the HTML file
file_path = "downloaded_pages/coolshop.html"
with open(file_path, "r") as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.parse(file_path, parser)

# Scrape the featured articles from the blog section
articles = tree.xpath("/html/body/div[1]/section[17]/div")
data = []
for article in articles:
    title = article.xpath(".//h2/text()")[0]
    content = article.xpath(".//p/text()")[0]
    data.append([title, content])

# Save the scraped data as a CSV file
output_file = "scraped_data.csv"
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Content"])
    writer.writerows(data)