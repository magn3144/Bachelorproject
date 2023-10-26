import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/bbc_weather.html', 'r') as file:
    html_content = file.read()

# Create an lxml HTML parser
parser = etree.HTMLParser()
tree = etree.parse(html_content, parser)

# Find the Weather Watchers title using XPath
title_xpath = '/html/body/div[8]/div/div[7]/div/h2'  # Update the XPath here if needed
title_element = tree.xpath(title_xpath)[0]
title = title_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Weather Watchers Title'])
    writer.writerow([title])