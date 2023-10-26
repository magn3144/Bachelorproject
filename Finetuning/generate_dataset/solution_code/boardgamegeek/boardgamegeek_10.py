import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/boardgamegeek.html', 'r') as f:
    html_content = f.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Extract the non-gaming forums and their descriptions
non_gaming_forums = html_tree.xpath('//gg-forum-listing[not(div/a[contains(text(), "BGG Store")])]/div/div[1]/dl/div[1]/dt/span/text()')
descriptions = html_tree.xpath('//gg-forum-listing[not(div/a[contains(text(), "BGG Store")])]/div/div[1]/dl/div[2]/dd/text()')

# Combine the data into a list of tuples
data = list(zip(non_gaming_forums, descriptions))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Forum', 'Description'])
    writer.writerows(data)