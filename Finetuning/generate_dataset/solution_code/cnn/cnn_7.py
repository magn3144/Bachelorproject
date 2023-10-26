import csv
import requests
from lxml import html

# Define the target URL and category
url = 'https://www.cnn.com'
category = 'News'

# Download the HTML page
response = requests.get(url)
html_content = response.content

# Parse the HTML content
tree = html.fromstring(html_content)

# Retrieve the text from the ad feedback link label
xpath = '/html/body/div[1]/section[3]/section[1]/div/section/div/div/div/div[3]/div/div[3]/div/div[2]/div[2]/div'
feedback_link = tree.xpath(xpath)[0].text_content().strip()

# Save the scraped data as a CSV file
data = [{'Category': category, 'Feedback Link Label': feedback_link}]
csv_filename = 'scraped_data.csv'

with open(csv_filename, 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)