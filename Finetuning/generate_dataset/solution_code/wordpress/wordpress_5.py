import csv
import requests
from lxml import html

# Define the target HTML file path
html_file_path = 'downloaded_pages/wordpress.html'

# Define the XPath for the desired heading element
target_xpath = '/html/body/div/main/div[2]/div/div[1]/h1'

# Load the HTML file and parse it
with open(html_file_path, 'r') as file:
    html_content = file.read()
tree = html.fromstring(html_content)

# Find the text content of the target heading element
heading_text = tree.xpath(target_xpath)[0].text_content()

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Heading'])
    writer.writerow(['Blogs', heading_text])

print("Scraping completed and data saved as 'scraped_data.csv'.")