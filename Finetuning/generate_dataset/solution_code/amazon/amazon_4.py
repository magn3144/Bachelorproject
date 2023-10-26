import csv
from lxml import etree

# Define the paths to the HTML file and the CSV file
html_path = 'downloaded_pages/amazon.html'
csv_path = 'scraped_data.csv'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_path, parser)

# Define the XPaths for the height elements
height_xpath_1 = '/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[7]/div[14]/span'
height_xpath_2 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[24]/div/div/div/div/div/div[2]/div/div/div[2]/div/span[1]/span/a/i[1]/span'

# Get the height values from the HTML using the XPaths
height_1_element = tree.xpath(height_xpath_1)[0]
height_1 = height_1_element.text if height_1_element is not None else ''
height_2_element = tree.xpath(height_xpath_2)[0]
height_2 = height_2_element.text if height_2_element is not None else ''

# Define the list of height values
heights = [height_1, height_2]

# Write the heights to the CSV file
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Height from Surface to Top'])
    writer.writerow(heights)