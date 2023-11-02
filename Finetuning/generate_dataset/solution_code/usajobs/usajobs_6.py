```
import csv
from lxml import etree

# Define the XPaths for the search feature titles and descriptions
xpath_titles = "/html/body/section/section/div/main/div[5]/div[5]/h2"
xpath_descriptions = "/html/body/section/section/div/main/div[5]/div[5]/p"

# Parse the HTML file
tree = etree.parse("downloaded_pages/usajobs.html")

# Extract the titles and descriptions using XPaths
titles = tree.xpath(xpath_titles)
descriptions = tree.xpath(xpath_descriptions)

# Zip the titles and descriptions into a list of tuples
data = list(zip(titles, descriptions))

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Description'])  # Write header row
    writer.writerows(data)
```