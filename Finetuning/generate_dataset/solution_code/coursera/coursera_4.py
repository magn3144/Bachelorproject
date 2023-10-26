import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/coursera.html', 'r') as file:
    html_data = file.read()

# Parse the HTML
html_tree = etree.HTML(html_data)

# Extract the titles of certificate programs
titles = html_tree.xpath('/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[5]/div/section/div/div[2]/div[1]/div[2]/div/p/text()')

# Create a CSV file and write the titles
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Certificate Program Titles'])
    for title in titles:
        writer.writerow([title])