import csv
from lxml import etree

# Define the target HTML file path
html_file_path = "downloaded_pages/espn.html"

# Define the list of XPaths for scores and networks
score_xpaths = [
    '/html/body/div[1]/div/div/div/main/div[3]/div/div[2]/div/aside[2]/section/div/div/div[2]/a/div/h2',
    '/html/body/div[1]/div/div/div/main/div[3]/div/div[2]/div/aside[2]/section/div/div/div[3]/a/div/div'
]
network_xpaths = [
    '/html/body/div[1]/div/div/div/main/div[3]/div/div[2]/div/aside[2]/section/div/div/div[2]/a/div/div/div',
    '/html/body/div[1]/div/div/div/main/div[3]/div/div[2]/div/aside[2]/section/div/div/div[3]/a/div/ul/li'
]

# Load the HTML file
with open(html_file_path, 'r') as f:
    html_content = f.read()
    tree = etree.HTML(html_content)

# Extract scores and networks using XPaths
scores = [score.text for score in tree.xpath('|'.join(score_xpaths))]
networks = [network.text for network in tree.xpath('|'.join(network_xpaths))]

# Combine scores and networks into a list of tuples
data = list(zip(scores, networks))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Score', 'Network'])
    writer.writerows(data)