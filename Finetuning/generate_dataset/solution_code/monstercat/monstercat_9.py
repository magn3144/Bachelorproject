import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/monstercat.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find the Explore properties section
explore_properties_xpath = '/html/body/div[4]/footer/div[1]/div[1]/section[1]/h3'
explore_properties = tree.xpath(explore_properties_xpath)

# Extract the property names
property_names = [prop.text_content() for prop in explore_properties]

# Write the property names to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Property Name'])
    writer.writerows(property_names)