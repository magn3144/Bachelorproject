import csv
from lxml import etree

# Define the HTML file path
html_file = 'downloaded_pages/y8.html'

# Define the XPath expressions for the elements containing the number of plays
xpaths = [
    '/html/body/div[1]/div[5]/div[2]/ul/li[11]/a/div[2]/div[3]/text()',
    '/html/body/div[1]/div[5]/div[2]/ul/li[16]/a/div[2]/div[3]/text()',
    '/html/body/div[1]/div[5]/div[2]/ul/li[4]/a/div[2]/div[3]/text()',
    '/html/body/div[1]/div[5]/div[2]/ul/li[28]/a/div[2]/div[2]/span/text()',
    '/html/body/div[1]/div[5]/div[2]/ul/li[50]/a/div[2]/div[3]/text()',
]

# Extract the number of plays from the HTML file
plays = []
with open(html_file, 'r') as file:
    html = file.read()
    tree = etree.HTML(html)
    for xpath in xpaths:
        play = tree.xpath(xpath)
        if len(play) > 0:
            plays.append(play[0].strip())

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Number of Plays'])
    writer.writerows(zip(plays))