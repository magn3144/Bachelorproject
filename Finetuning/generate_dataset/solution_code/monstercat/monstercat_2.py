import csv
from lxml import etree

# Define the target HTML file path
html_path = "downloaded_pages/monstercat.html"

# Define the XPath for the list of EPs
xpath_ep_list = "/html/body/div[4]/div[4]/div[3]/main/div[3]/div/div/table/tbody/tr/td[2]/a"
   
# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_path, parser)

# Find all elements matching the XPath for EPs
eps = tree.xpath(xpath_ep_list)

# Extract the titles of the EPs
ep_titles = [ep.text.strip() for ep in eps]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['EP Title'])
    writer.writerows([[title] for title in ep_titles])