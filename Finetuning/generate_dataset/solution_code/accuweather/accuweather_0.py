import csv
from lxml import etree

# Define the XPaths of the elements to be scraped
xpaths = {
    "location": "/html/body/div/div[1]/div[1]/div/a[2]/h1",
    "forecast": "/html/body/div/div[7]/div[1]/div[1]/a[1]/div[2]/span[1]"
}

# Read the HTML file
tree = etree.parse("downloaded_pages/accuweather.html")

# Scrape the elements using the XPaths
location = tree.xpath(xpaths["location"])[0].text.strip()
forecast = tree.xpath(xpaths["forecast"])[0].text.strip()

# Prepare the data to be written in CSV file
data = [
    ["Location", "Forecast"],
    [location, forecast]
]

# Write the data into CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)