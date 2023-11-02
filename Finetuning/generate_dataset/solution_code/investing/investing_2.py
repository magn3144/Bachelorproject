import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/investing.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Scrape the popular searches for stocks
popular_searches = tree.xpath('/html/body/div/header/div[1]/section/div[2]/div[2]/div[1]/div/header/h4/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Popular Searches'])
    writer.writerow(popular_searches)