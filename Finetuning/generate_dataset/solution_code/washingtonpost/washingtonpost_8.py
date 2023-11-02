import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/washingtonpost.html', 'r') as file:
    html_str = file.read()

# Create an HTML tree from the string
tree = html.fromstring(html_str)

# Find the headlines and their dates
headlines = tree.xpath('//div[contains(@class, "wpds-c-fJKSbB")]/text()')
dates = tree.xpath('//div[contains(@class, "bold") and contains(@class, "font-xs")]/text()')

# Combine headlines and dates into a list of tuples
data = list(zip(headlines, dates))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'Date'])
    writer.writerows(data)