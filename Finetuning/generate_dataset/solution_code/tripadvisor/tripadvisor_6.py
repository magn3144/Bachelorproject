import csv
from lxml import etree

# Read the HTML file
with open("downloaded_pages/tripadvisor.html", "r") as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all sushi restaurants in Vejen
sushi_restaurants = tree.xpath("//a[contains(text(), 'Sushi restauranter i Vejen')]")

# Extract the names of sushi restaurants
names = [restaurant.text for restaurant in sushi_restaurants]

# Save the data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Restaurant Name"])
    writer.writerows(names)