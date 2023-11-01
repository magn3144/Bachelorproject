import csv
from lxml import etree

# Define the target XPath for the section with "Myspace Exclusives"
section_xpath = "/html/body/div[1]/div[2]/div[1]/section[5]"

# Read the HTML file
with open('downloaded_pages/myspace.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Find the section with "Myspace Exclusives"
section = tree.xpath(section_xpath)[0]

# Find all the song titles within the section
song_titles = section.xpath(".//h4[@class='description']/text()")

# Write the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Song Title'])
    writer.writerows(zip(song_titles))