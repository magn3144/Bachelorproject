import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/9gag.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
parsed_html = html.fromstring(html_content)

# Find all the post captions or descriptions
post_captions = parsed_html.xpath('//div[@class="post-caption"]/text()')

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Post Captions'])

    for caption in post_captions:
        writer.writerow([caption])