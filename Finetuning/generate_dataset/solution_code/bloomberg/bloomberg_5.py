import csv
from lxml import etree

# Define the function to retrieve the captions
def retrieve_captions(html_path):
    # Load the HTML file
    with open(html_path, 'r') as f:
        html_content = f.read()

    # Parse the HTML content
    tree = etree.HTML(html_content)

    # Find all the video captions using XPaths
    captions = tree.xpath('//span[@class="vjs-control-text"]/text()')

    return captions

# Set the local path to the HTML file
html_path = 'downloaded_pages/bloomberg.html'

# Retrieve the captions
captions = retrieve_captions(html_path)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Caption'])

    for caption in captions:
        writer.writerow([caption])