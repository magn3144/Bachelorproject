import csv
from lxml import etree

# Define the HTML file path
html_file_path = 'downloaded_pages/census.html'

# Define the XPaths of the target element
data_maps_xpath = '/html/body/div[3]/div/div/div[3]/header/div[1]/div[2]/div[2]/div[1]/div[2]/a'

# Open the HTML file
with open(html_file_path, 'r') as file:
    # Parse the HTML
    html = etree.parse(file)

# Find the target element using XPath
data_maps_element = html.xpath(data_maps_xpath)

# Extract the text from the element
data_maps_link = data_maps_element[0].text.strip()

# Save the scraped data as a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Data & Maps Link'])
    writer.writerow([data_maps_link])

print('Scraping completed and data saved as "scraped_data.csv".')