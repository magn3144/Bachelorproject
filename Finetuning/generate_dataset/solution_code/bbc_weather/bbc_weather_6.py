import csv
from lxml import etree

# Define the XPath expressions for the target elements
xpath_report_header = '/html/body/div[8]/div/div[7]/div/h2'
xpath_report = '/html/body/div[8]/div/div[7]/div/div/div[4]/a/p'

# Parse the HTML file
html_tree = etree.parse('downloaded_pages/bbc_weather.html', etree.HTMLParser())

# Extract the report header
report_header_element = html_tree.xpath(xpath_report_header)[0]
report_header = report_header_element.text.strip()

# Extract the report
report_element = html_tree.xpath(xpath_report)[0]
report = report_element.text.strip()

# Write the scraped data to CSV
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Report Header', 'Report'])
    writer.writerow([report_header, report])