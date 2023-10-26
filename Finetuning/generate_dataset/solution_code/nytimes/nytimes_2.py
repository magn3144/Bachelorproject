import csv
import re
from lxml import html

# Define the XPath for the dates of the articles in the main section
date_xpath = '/html/body/div/div[2]/main/section/div[1]/section[1]/div[1]/ol/li//span[contains(@class, "")]'

# Load the HTML file
with open('downloaded_pages/nytimes.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Extract the dates using XPath
dates_elements = tree.xpath(date_xpath)

# Extract the text from the date elements
dates_text = [date_element.text_content().strip() for date_element in dates_elements]

# Remove any empty strings or extra whitespace
dates_text = [re.sub(r'\s{2,}', ' ', date) for date in dates_text if date]

# Save the dates as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date'])
    writer.writerows([[date] for date in dates_text])