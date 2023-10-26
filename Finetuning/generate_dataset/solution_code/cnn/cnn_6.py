import csv
from lxml import etree

# Open the HTML file
with open("downloaded_pages/cnn.html", "r") as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Get the text from the CNN Analysis section
xpaths = [
    "/html/body/div[1]/section[3]/section[1]/div/section/div/div/div/div[2]/div/h2",
    "/html/body/div[1]/section[3]/section[1]/div/section/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[3]/h2",
    "/html/body/div[1]/section[3]/section[1]/div/section/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[3]/h2"
]

text = ""
for xpath in xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        text += element.text.strip() + " "

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([text])