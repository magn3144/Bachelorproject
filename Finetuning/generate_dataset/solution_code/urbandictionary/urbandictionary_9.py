import requests
import csv
from lxml import html

# Define the target URL
url = "https://www.urbandictionary.com/"

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content
tree = html.fromstring(html_content)

# Find the XPath of the "Ghetto Baby" link
xpath = "/html/body/div/div/main/div/div[4]/section/div[9]/div/div[2]/a[1]"

# Extract the link text and its XPath from the target page
link = tree.xpath(xpath)[0].text_content()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link', 'XPath'])
    writer.writerow([link, xpath])