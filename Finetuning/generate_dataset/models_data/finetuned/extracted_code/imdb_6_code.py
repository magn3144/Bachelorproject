
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all the h3 elements under "more to explore"
h3_elements = tree.xpath('//div[@class="more-to-explore"]/h3')

# Create a list to store the scraped data
scraped_data = []

# Iterate over the h3 elements
for h3_element in h3_elements:
    # Get the text of the h3 element
    h3_text = h3_element.text

    # Get the link of the h3 element
    a_element = h3_element.xpath('./a')[0]
    link = a_element.attrib['href']

    # Save the data as a list
    scraped_data.append([h3_text, link])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Headline', 'Link'])
    writer.writerows(scraped_data)
