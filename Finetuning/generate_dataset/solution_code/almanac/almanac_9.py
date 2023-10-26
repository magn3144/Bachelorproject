import csv
from lxml import html

# Define the HTML file path
html_path = "downloaded_pages/almanac.html"

# Define the XPath for the product names and prices
product_name_xpath = "//div[@class='social-bar']//a[@class='menu__link menu__link--link menu__link--level-1' and text()='Free Daily Newsletter']"
product_price_xpath = "//div[@class='social-bar']//div[@class='a2a_localize']"

# Load the HTML file
with open(html_path, "r") as f:
    html_content = f.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Scrape the product names
product_names = tree.xpath(product_name_xpath)[0].text

# Scrape the product prices
product_prices = tree.xpath(product_price_xpath)[0].text

# Prepare the data to be saved as a CSV file
data = [
    {"Product Name": product_names.strip(), "Product Price": product_prices.strip()}
]

# Save the data as a CSV file
csv_file = "scraped_data.csv"
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Product Name", "Product Price"])
    writer.writeheader()
    writer.writerows(data)