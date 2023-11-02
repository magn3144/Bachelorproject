import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/walmart.html', 'r') as f:
    page_content = f.read()
    
# Parse the HTML
tree = html.fromstring(page_content)

# Find the elements containing the prices and sizes of honeycrisp apples
price_elements = tree.xpath("//span[contains(text(), 'Honeycrisp')]/following-sibling::div[@class='mr1 mr2-xl b black lh-copy f5 f4-l']")
size_elements = tree.xpath("//span[contains(text(), 'Honeycrisp')]/preceding-sibling::span[@class='normal dark-gray mb0 mt1 lh-title f6 f5-l']")

# Extract the prices and sizes as lists
prices = [element.text.strip() for element in price_elements]
sizes = [element.text.strip() for element in size_elements]

# Combine the prices and sizes into a list of tuples
data = list(zip(prices, sizes))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Price', 'Size'])
    writer.writerows(data)