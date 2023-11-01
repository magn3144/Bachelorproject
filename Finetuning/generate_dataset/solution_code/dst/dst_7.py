import csv
from lxml import html

# Define the XPaths for the target elements
xpath_divorces = "/html/body/div[1]/main/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]"
xpath_development = "/html/body/div[1]/main/div/div[2]/div[1]/div/div/div[3]/div[2]/div/h2"

# Load the HTML file
with open('downloaded_pages/dst.html', 'r') as f:
    webpage = f.read()

# Parse the HTML
tree = html.fromstring(webpage)

# Find the number of divorces
divorces_element = tree.xpath(xpath_divorces)[0]
divorces = divorces_element.text_content().strip()

# Find the development in the number of divorces
development_element = tree.xpath(xpath_development)[0]
development = development_element.text_content().strip()

# Create a dictionary with the scraped data
data = {'Divorces': divorces, 'Development': development}

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Divorces', 'Development'])
    writer.writeheader()
    writer.writerow(data)