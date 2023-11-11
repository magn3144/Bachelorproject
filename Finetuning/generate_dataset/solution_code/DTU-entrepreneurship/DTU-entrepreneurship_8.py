import csv
from lxml import etree

# Parse the HTML file
tree = etree.parse('downloaded_pages/DTU-entrepreneurship.html')
root = tree.getroot()

# Find the desired paragraph using XPath
paragraph_xpath = '/html/body/form/div[3]/div[5]/div[2]/div/div[2]/div/p'
paragraph_element = root.xpath(paragraph_xpath)[0]

# Extract the text from the paragraph element
paragraph_text = paragraph_element.text.strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([paragraph_text])