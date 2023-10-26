import csv
from bs4 import BeautifulSoup

# Define the local path to the HTML file
html_file = 'downloaded_pages/aboutus.html'

# Define the category of the page
category = 'Directories'

# Define the XPath expressions for the contact details
xpaths = [
    '/html/body/section/div[3]/div[1]/div/div[2]/div[1]/div[2]/h2[4]/span',
    '/html/body/section/div[3]/div[1]/div/div[2]/div[1]/div[2]/dl[2]/dd[1]',
    '/html/body/section/div[3]/div[1]/div/div[2]/div[1]/div[2]/dl[2]/dd[4]',
    '/html/body/section/div[3]/div[1]/div/div[2]/div[1]/div[1]/div[3]/div[4]/div[2]'
]

# Extract the contact details using the XPaths
with open(html_file) as file:
    soup = BeautifulSoup(file, 'html.parser')
    data = [soup.select_one(xpath).text.strip() for xpath in xpaths]

# Save the scraped data in a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Contact 1', 'Contact 2', 'Contact 3', 'Contact 4'])
    writer.writerow([category] + data)