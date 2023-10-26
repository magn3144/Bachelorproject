import csv
from lxml import html

# Define the XPath expressions for the captions of the images in the first article
image_captions_xpath = '/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[1]/div/article/figure/figcaption'

# Read the HTML file
with open('downloaded_pages/nytimes.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Extract the image captions
image_captions_elements = tree.xpath(image_captions_xpath)
image_captions = [elem.text_content().strip() for elem in image_captions_elements]

# Write the image captions to a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Image Caption'])
    writer.writerows([[caption] for caption in image_captions])