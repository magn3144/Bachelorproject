import csv
import os
from lxml import etree

# Set file paths
html_file_path = 'downloaded_pages/edx.html'
csv_file_path = 'scraped_data.csv'

# Define the XPaths
google_cloud_xpath = '/html/body/div[1]/div[1]/div/main/div/div[5]/div/div[3]/div[23]/a/div/div[2]/div/div[1]/span/span[1]/span[1]'

# Open the HTML file
with open(html_file_path, 'r') as file:
    html_data = file.read()

# Parse the HTML
tree = etree.HTML(html_data)

# Extract the text using the XPath
google_cloud_text = tree.xpath(google_cloud_xpath)[0].text

# Check if the CSV file already exists
if os.path.exists(csv_file_path):
    # Append data to existing CSV file
    with open(csv_file_path, 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([google_cloud_text])
else:
    # Create a new CSV file and write the data
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Google Cloud Computing'])
        writer.writerow([google_cloud_text])