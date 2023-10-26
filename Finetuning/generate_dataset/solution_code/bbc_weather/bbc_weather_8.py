import csv
from lxml import etree

# Define the target HTML file path
html_file_path = 'downloaded_pages/bbc_weather.html'

# Load the HTML file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML
html_tree = etree.HTML(html_content)

# Extract the "Remember the places that matter to you" title
title_element = html_tree.xpath('/html/body/div[8]/div/div[1]/div/div/div[2]/div/div/div/div[5]/div[2]/div/div/h4')[0]
title = title_element.text.strip()

# Save the scraped data as a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerow([title])