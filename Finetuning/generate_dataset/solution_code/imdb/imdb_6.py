import csv
import lxml.html as html_parser

# open source file
with open('downloaded_pages/imdb.html', 'r') as file:
    webpage = file.read().replace('\n', '')

# parse html
parsed_webpage = html_parser.fromstring(webpage)

# xpaths to the target elements
xpaths = ['//*[@class="ipc-title__description"]', '//*[@class="ipc-title__text chart-layout-specific-title-text"]']

# find elements
elements = []
for xpath in xpaths:
    elements += parsed_webpage.xpath(xpath)

# get element text
data = [el.text_content() for el in elements]

# write to csv file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Descriptions"])
    for description in data:
        writer.writerow([description])