import csv
from lxml import etree

# Read the HTML file
html_path = 'downloaded_pages/ziprecruiter.html'
with open(html_path, 'r') as f:
    html_content = f.read()

# Create an ElementTree from the HTML content
tree = etree.HTML(html_content)

# Define the XPaths for the footer titles and details
footer_title_xpath = '/html/body/footer/div/div[1]/div/nav/h3'
footer_detail_xpath = '/html/body/footer/div/div[1]/div/nav/div/div/h3'

# Extract the footer titles and details
footer_titles = tree.xpath(footer_title_xpath)
footer_details = tree.xpath(footer_detail_xpath)

# Save the scraped data as a CSV file
csv_path = 'scraped_data.csv'
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Detail'])
    for title, detail in zip(footer_titles, footer_details):
        writer.writerow([title.text.strip(), detail.text.strip()])