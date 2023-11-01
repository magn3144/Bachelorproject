import csv
from lxml import html

# Define the xpath expressions for the elements containing the desired details
dimensions_xpath = "//div[contains(text(), 'Dimensions:')]/following-sibling::div"
colors_xpath = "//div[contains(text(), 'Colors:')]/following-sibling::div"
materials_xpath = "//div[contains(text(), 'Materials:')]/following-sibling::div"

# Parse the HTML file
with open("downloaded_pages/normal.html", "r") as file:
    content = file.read()
tree = html.fromstring(content)

# Scrape the data from the HTML elements using the xpath expressions
dimensions = tree.xpath(dimensions_xpath)
colors = tree.xpath(colors_xpath)
materials = tree.xpath(materials_xpath)

# Zip the scraped data into a list of tuples
scraped_data = list(zip(dimensions, colors, materials))

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Dimensions", "Colors", "Materials"])  # Write the header
    writer.writerows(scraped_data)