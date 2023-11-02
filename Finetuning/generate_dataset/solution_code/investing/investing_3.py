import csv
from lxml import html

# Define the target XPath for cryptocurrency names
cryptocurrency_xpath = "/html/body/div/div[2]/div/div/div/main/div[6]/div[1]/div/div/table/tbody//div[contains(@class, 'crypto-coins-table_cellNameText__aaXmK')]"

# Parse the HTML file
with open('downloaded_pages/investing.html', 'r') as file:
    content = file.read()
    tree = html.fromstring(content)

# Scrape the cryptocurrency names
cryptocurrencies = tree.xpath(cryptocurrency_xpath)

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Cryptocurrency'])
    writer.writerows([[name.text.strip()] for name in cryptocurrencies])