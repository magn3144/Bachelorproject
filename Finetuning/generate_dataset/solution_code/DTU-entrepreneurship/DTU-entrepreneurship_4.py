import csv
from pathlib import Path
from lxml import etree

# Load the HTML file
path = Path("downloaded_pages/DTU-entrepreneurship.html")
html = etree.parse(str(path), etree.HTMLParser())

# Find the education link using XPath
education_link = html.xpath("/html/body/form/div[3]/div[5]/div[1]/div/div/div/a[2]")[0].text

# Save the extracted text as a CSV file
data = [[education_link]]
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)