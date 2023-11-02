import csv
from lxml import etree

# Define the HTML elements and their XPaths
html_elements = {
    "trending_tickers": '/html/body/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/ul/li/div/div/div/h3/a/span'
}

# Read the HTML file
with open('downloaded_pages/finance.yahoo.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = etree.HTML(html_content)

# Scrape the trending tickers
trending_tickers = tree.xpath(html_elements['trending_tickers'])

# Prepare the data to be saved as CSV
data = [[ticker.text] for ticker in trending_tickers]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)