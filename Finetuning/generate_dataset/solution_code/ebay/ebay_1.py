import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/ebay.html', 'r') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find the Expand Cart button
expand_cart_xpath = '/html/body/div[3]/header/div/ul[2]/li[6]/div/a[2]'
expand_cart_button = tree.xpath(expand_cart_xpath)[0]

# Click the Expand Cart button
# (Assuming the clicking action is not simulated in this script)

# Retrieve the cart items
cart_items_xpath = '/html/body/div[3]/header/div/ul[2]/li[6]/div/div/div/div'
cart_items = tree.xpath(cart_items_xpath)

# Extract the text from the cart items
cart_items_text = [item.text for item in cart_items]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Cart Items'])
    writer.writerows(cart_items_text)