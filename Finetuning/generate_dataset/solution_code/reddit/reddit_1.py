import csv
import requests
from lxml import html

# Define the target URL and local path to the HTML file
url = 'https://www.reddit.com/'
local_path = 'downloaded_pages/reddit.html'

# Open the local HTML file and create an HTML tree
with open(local_path, 'r') as file:
    content = file.read()
tree = html.fromstring(content)

# Define the XPath expressions for the user account menu details
xpath_expressions = [
    '/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/div[2]/div/div[2]/button/span[2]',
    '/html/body/div[1]/div/div[2]/div[1]/header/div/div[1]/div[3]/div/form/label/span'
]

# Scrape the user account menu details using the XPath expressions
user_account_menu_details = []
for xpath_expression in xpath_expressions:
    elements = tree.xpath(xpath_expression)
    if len(elements) > 0:
        user_account_menu_details.append(elements[0].text)
    else:
        user_account_menu_details.append('')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(user_account_menu_details)