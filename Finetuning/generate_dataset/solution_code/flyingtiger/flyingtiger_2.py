import csv
from lxml import html

# Parse the HTML file
tree = html.parse('downloaded_pages/flyingtiger.html')

# Find all <div> tags with class "h5"
div_elements = tree.xpath('//div[@class="h5"]')

# Extract the text from each div element
scraped_data = [div.text_content().strip() for div in div_elements]

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Scraped Text'])
    writer.writerows(zip(scraped_data))