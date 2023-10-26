import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/etsy.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
root = etree.HTML(html_content)

# Find the element using XPath
element_xpath = "/html/body/main/div/div[8]/div/div/div[2]/div[1]/div[3]/div[1]/legend"
element = root.xpath(element_xpath)

# Extract the text content
text_content = element[0].text.strip()

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text Content'])
    writer.writerow([text_content])