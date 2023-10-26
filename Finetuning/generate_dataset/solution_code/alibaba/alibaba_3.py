import csv
from lxml import etree

# Define the XPaths for the target elements
xpaths = [
    "/html/body/div[3]/div[1]/div/div[4]/div[2]/div/div/div/div[25]/div[2]/div[1]/a[2]/div/div",  
    "/html/body/div[3]/div[1]/div/div[4]/div[2]/div/div/div/div[16]/div[2]/div[1]/a[3]/div/div",
    "/html/body/div[3]/div[1]/div/div[4]/div[2]/div/div/div/div[45]/div[2]/div[1]/a[3]/div/div[1]",
    "/html/body/div[3]/div[1]/div/div[4]/div[2]/div/div/div/div[27]/div[2]/div[1]/a[2]/div/div"
]

# Parse the HTML file
html = etree.parse("downloaded_pages/alibaba.html", etree.HTMLParser())

# Initialize an empty list to store the scraped data
scraped_data = []

# Loop through the XPaths and extract the text content of each element
for xpath in xpaths:
    elements = html.xpath(xpath)
    for element in elements:
        scraped_data.append(element.text.strip())

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Price'])
    writer.writerows([[data] for data in scraped_data])