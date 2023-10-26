import csv
from pathlib import Path
from lxml import etree

# Load the HTML file
html_file = Path("downloaded_pages/cnn.html")
html_tree = etree.parse(str(html_file))

# Define the XPaths for image credits in Fault Lines section
image_credit_xpath = '/html/body/div[1]/section[3]/section[1]/div/section/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div/h2/following-sibling::a/div/div/div/div[2]/figcaption'

# Find image credits in Fault Lines section
image_credits = html_tree.xpath(image_credit_xpath)

# Write scraped data to CSV file
csv_file = "scraped_data.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Image Credit"])
    for credit in image_credits:
        writer.writerow([credit.text.strip()])