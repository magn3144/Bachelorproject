import csv
from lxml import etree

# Define the XPath for the element containing the main content
main_content_xpath = "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div"

# Parse the HTML file
html_parser = etree.HTMLParser()
tree = etree.parse('downloaded_pages/finance.yahoo.html', html_parser)

# Find the main content element using XPath
main_content_element = tree.xpath(main_content_xpath)[0]

# Get the text content of the main content element
main_content = main_content_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Main Content'])
    writer.writerow([main_content])