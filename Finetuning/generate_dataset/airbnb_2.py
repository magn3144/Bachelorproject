import csv
from lxml import html
from lxml.html import fromstring

# Load the HTML data from local file.
with open('downloaded_pages/airbnb.html', 'r') as file:
    page_content = file.read().replace('\n', '')

tree = html.fromstring(page_content)

# XPaths for location elements and distance elements
location_xpath = "//div[contains(@class, 't1jojoys dir dir-ltr')]"
distance_xpath = "//span[contains(@class, 'a8jt5op dir dir-ltr')]"

locations = tree.xpath(location_xpath)
distances = tree.xpath(distance_xpath)

data = []

for location, distance in zip(locations, distances):
    data.append({"Location": location.text, "Distance": distance.text})

keys = data[0].keys()

# Save the scraped data in a CSV file
with open('scraped_data.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)