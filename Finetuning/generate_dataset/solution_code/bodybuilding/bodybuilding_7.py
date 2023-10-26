import csv
from lxml import html

# Define the HTML file path
html_file_path = 'downloaded_pages/bodybuilding.html'

# Define the XPaths for the author names
author_name_xpaths = [
    ("/html/body/section/main/bb-testimonials-slider/section/bb-testimonials-slide[1]/div/article/div[2]/div/div[1]", "Dawn Desarmeau"),
    ("/html/body/section/main/bb-testimonials-slider/section/bb-testimonials-slide[2]/div/article/div[2]/div/div[1]", "Catherine Krauter"),
    ("/html/body/section/main/bb-testimonials-slider/section/bb-testimonials-slide[1]/div/article/div[2]/div/div[1]", "Ashwin Prasad")
]

# Create a list to store the scraped data
scraped_data = []

# Parse the HTML file
tree = html.parse(html_file_path)

# Scrape the author names using the XPaths
for xpath, author_name in author_name_xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        scraped_data.append((author_name, xpath))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Author Name", "XPath"])
    writer.writerows(scraped_data)