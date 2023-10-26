import csv
from lxml import etree

# Define the XPaths for the gaming keyboard products and their features
keyboard_xpath = "//span[contains(@class, 'a-size-medium') and contains(@class, 'a-color-base') and contains(@class, 'a-text-normal')]"
features_xpath = "//div[contains(@class, 'a-section') and contains(@class, 'sbv-d-asin-info') and contains(@class, 's-underline-text')]"

# Load the HTML file
with open('downloaded_pages/amazon.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Extract the gaming keyboard products and their features
keyboards = tree.xpath(keyboard_xpath)
features = tree.xpath(features_xpath)

# Initialize a list to store the scraped data
data = []

# Iterate over the gaming keyboard products and their features to extract the text
for keyboard, feature in zip(keyboards, features):
    keyboard_text = keyboard.text.strip()
    feature_text = feature.text.strip()

    # Append the scraped data to the list
    data.append([keyboard_text, feature_text])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product', 'Feature'])
    writer.writerows(data)