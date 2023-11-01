import csv
from lxml import etree

# Define the target HTML file path
html_file_path = 'downloaded_pages/coolshop.html'

# Define the scraped data
scraped_data = []

# Open the HTML file and parse it into an lxml tree
with open(html_file_path, 'r') as html_file:
    tree = etree.parse(html_file)

    # Retrieve the titles and links related to different age-based toy categories
    categories = tree.xpath("//li[@class='title submenu__column__list-item' and starts-with(text(), 'Shop legetøj efter alder')]")
    for category in categories:
        title = category.text.strip()
        link = category.xpath("./a/@href")
        scraped_data.append([title, link])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(scraped_data)