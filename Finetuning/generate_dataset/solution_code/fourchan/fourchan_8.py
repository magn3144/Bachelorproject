import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/4chan.html', 'r') as file:
    html_content = file.read()

# Create the CSV file and write the headers
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Link', 'XPath'])

# Parse the HTML content
tree = html.fromstring(html_content)

# Find all feedback links and their XPaths
feedback_links = tree.xpath('//a[contains(text(), "Feedback")]/@href')
feedback_xpaths = tree.xpath('//a[contains(text(), "Feedback")]/ancestor-or-self::*[last()]/descendant::*/ancestor-or-self::*[last()]/@xpath')

# Append the scraped data to the CSV file
with open('scraped_data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(zip(feedback_links, feedback_xpaths))