import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/finviz.html', 'r') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all company names
company_names = tree.xpath('/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr/td[3]/a/text()')

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name'])
    writer.writerows(zip(company_names))