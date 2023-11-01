from lxml import etree
import csv

# Load the HTML file
file_path = 'downloaded_pages/google.html'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
html = etree.HTML(content)

# Find the "More Doodles" section
more_doodles_section = html.xpath('/html/body/div[2]/div/div[2]/h3')

# Retrieve the titles of other Doodles
doodle_titles = []
if more_doodles_section:
    doodles = more_doodles_section[0].getparent().getnext().xpath('./div/h3')
    for doodle in doodles:
        doodle_titles.append(doodle.text.strip())

# Save the scraped data as a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Doodle Title'])
    writer.writerows([title] for title in doodle_titles)