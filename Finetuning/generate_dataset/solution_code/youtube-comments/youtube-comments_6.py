import csv
from lxml import etree

# Define the XPath for the duration element
duration_xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[3]/div[1]/div/div[6]/div[1]/ytd-video-primary-info-renderer/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]'

# Open the local HTML file
with open('downloaded_pages/youtube-comments.html', 'r') as f:
    html_content = f.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Extract the duration element text using XPath
duration_element = html_tree.xpath(duration_xpath)[0]
duration = duration_element.text.strip()

# Create a CSV file and write the duration to it
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Duration'])
    writer.writerow([duration])