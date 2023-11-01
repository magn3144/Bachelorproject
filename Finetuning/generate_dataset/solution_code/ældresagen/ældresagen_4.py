import csv
from lxml import html

# Define the XPaths for the target elements
xpaths = [
    ['/html/body/div[2]/main/div[3]/div/div[1]/div/a/div[2]', 'div'],
    ['/html/body/div[2]/main/section[1]/section[2]/article/header/div/p', 'p']
]

# Create the CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category', 'Text'])

    # Parse the HTML file and extract the text from the target elements using the XPaths
    tree = html.parse('downloaded_pages/ældresagen.html')
    for xpath, elem_type in xpaths:
        elements = tree.xpath(xpath)
        for element in elements:
            text = element.text.strip()
            writer.writerow(['News', text])
