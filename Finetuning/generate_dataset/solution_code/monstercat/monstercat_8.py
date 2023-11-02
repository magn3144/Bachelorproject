import csv
from lxml import etree

# Read the HTML file
with open("downloaded_pages/monstercat.html", "r") as file:
    html_content = file.read()

# Create an lxml element tree
tree = etree.HTML(html_content)

# Find the popular pages section
popular_pages = tree.xpath('/html/body/div[4]/div[4]/div[3]/aside/div/div[3]/div/section//h2[contains(text(), "Popular Pages")]/following-sibling::ul/li/div/div[2]/div[1]/h4')

# Extract the page names
page_names = [page.text for page in popular_pages]

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Page Name"])
    writer.writerows(zip(page_names))