import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/booking.html', 'r') as file:
    html_data = file.read()

# Create an HTML parser
parser = etree.HTMLParser()
tree = etree.parse(html_data, parser)

# Define the XPaths for the amenities
amenity_xpaths = [
    "/html/body/div[13]/div[3]/div[1]/div/div/div[22]/div[3]/label/span[3]/div/div/div",
    "/html/body/div[5]/div/div[4]/div[1]/div[2]/div[1]/div/div/div[3]/div[19]/div[7]/label/span[3]/div/div/div",
    "/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[31]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[3]/span/span/div/span[2]",
    "/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[43]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[2]/div/span[2]/span/span",
    "/html/body/div[13]/div[3]/div[1]/div/div/div[13]/div[1]/h3",
    "/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/h2",
    "/html/body/div[13]/div[3]/div[1]/div/div/div[1]/h2",
    "/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[21]/div[1]/div[2]/div/div[3]/div[1]/div/div/div/h4",
    "/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[15]/div[1]/div[2]/div/div[3]/div[1]/div/div/div/h4",
    "/html/body/div[7]/div[1]/form/div/div[1]/div[4]/label",
    "/html/body/div[7]/div[3]/div[2]/div/div/div[3]/ul/li[4]/a",
    "/html/body/div[7]/div[3]/div[1]/div[2]/div/ul/li[1]/a",
    "/html/body/div[8]/div[2]/div/ul/li[5]/p",
    "/html/body/div[9]/div[1]/p[2]",
    "/html/body/div[9]/table/tbody/tr[1]/th[7]",
    "/html/body/div[9]/table/tbody/tr[3]/td[1]",
    "/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[49]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div[3]",
    "/html/body/div[5]/div/div[4]/div[1]/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[14]/label/span[3]/div/div/div",
    "/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[17]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[2]/div/a/span/span[1]",
    "/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[13]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[2]/div/a/span/span[1]",
    "/html/body/div[13]/div[3]/div[1]/div/div/div[7]/div[1]/h3",
    "/html/body/div[5]/div/div[4]/div[1]/div[2]/div[1]/div/div/div[3]/div[21]/div[1]/h3",
    "/html/body/div[8]/div[1]/h2",
    "/html/body/div[8]/div[2]/div/h2",
    "/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[19]/div[1]/div[2]/div/div[3]/div[1]/div/div/div/h4",
    "/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[17]/div[1]/div[2]/div/div[3]/div[1]/div/div/div/h4",
    "/html/body/div[7]/div[3]/div[2]/div/div/div[5]/ul/li[1]/a",
    "/html/body/div[7]/div[3]/div[2]/div/div/div[1]/ul/li[3]/a",
    "/html/body/div[8]/div[2]/div/ul/li[1]/p",
    "/html/body/div[8]/div[2]/div/ul/li[1]/p"
]

# Scrape the amenities
amenities = []
for xpath in amenity_xpaths:
    elements = tree.xpath(xpath)
    if len(elements) > 0:
        amenities.append(elements[0].text)
    else:
        amenities.append("N/A")

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Amenities'])
    writer.writerow(amenities)