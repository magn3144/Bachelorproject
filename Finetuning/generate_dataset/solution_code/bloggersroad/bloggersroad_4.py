from lxml import etree
import csv

# Define the local path to the HTML file
html_file_path = 'downloaded_pages/bloggersroad.html'

# Define the XPaths for the page navigation elements
current_page_xpath = '/html/body/div/div[1]/div/main/nav/div/span[1]'
total_pages_xpath = '/html/body/div/div[1]/div/main/nav/div/span[2]'

# Parse the HTML file
tree = etree.parse(html_file_path)

# Extract the page navigation information
current_page = tree.xpath(current_page_xpath)[0].text
total_pages = tree.xpath(total_pages_xpath)[0].text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Current Page', 'Total Pages'])
    writer.writerow([current_page, total_pages])