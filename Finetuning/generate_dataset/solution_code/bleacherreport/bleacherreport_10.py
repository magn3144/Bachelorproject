import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/bleacherreport.html', 'r') as f:
    html_content = f.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Find all the video titles using XPath
video_titles = html_tree.xpath('//h3[contains(@class, "text")]/text()')

# Write the video titles to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title'])
    writer.writerows([[title] for title in video_titles])