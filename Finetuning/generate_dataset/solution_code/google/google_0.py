import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/google.html', 'r') as f:
    html_content = f.read()

# Create the HTML tree
tree = html.fromstring(html_content)

# Define the XPaths for the doodle titles and dates
title_xpath = '/html/body/div[2]/div/ul/li/div/h2'
date_xpath = '/html/body/div[2]/div/ul/li/div/div'

# Extract the doodle titles and dates
titles = tree.xpath(title_xpath)
dates = tree.xpath(date_xpath)

# Create a list to store the scraped data
scraped_data = []

# Zip the titles and dates together and add them to the scraped data list
for title, date in zip(titles, dates):
    scraped_data.append([title.text_content().strip(), date.text_content().strip()])

# Save the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Date'])
    writer.writerows(scraped_data)