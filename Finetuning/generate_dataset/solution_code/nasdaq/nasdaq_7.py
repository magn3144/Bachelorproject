import csv
from lxml import etree

# Define the XPath expressions for the data extraction
xpath_monthly_data = "//h5[contains(@class, 'date-picker__month-year')]"
xpath_yearly_data = "//h5[contains(@class, 'market-calendar__title')]"

# Load the HTML file
html_file = "downloaded_pages/nasdaq.html"
tree = etree.parse(html_file)

# Extract the monthly and yearly data from the HTML
monthly_data = [element.text.strip() for element in tree.xpath(xpath_monthly_data)]
yearly_data = [element.text.strip() for element in tree.xpath(xpath_yearly_data)]

# Combine the monthly and yearly data
all_data = monthly_data + yearly_data

# Save the data in a CSV file
csv_file = "scraped_data.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Data"])
    writer.writerows([[data] for data in all_data])