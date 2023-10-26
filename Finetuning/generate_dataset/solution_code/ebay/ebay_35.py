import csv
from lxml import html

# Define the XPath for the target element
target_xpath = '/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[1]/div/span/div/div[194]/span'

# Read the HTML file
with open('downloaded_pages/ebay.html', 'r') as file:
    html_content = file.read()

# Create an ElementTree object from the HTML content
tree = html.fromstring(html_content)

# Extract the text of the target element using XPath
target_text = tree.xpath(target_xpath)[0].text.strip()

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([target_text])