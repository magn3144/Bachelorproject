import csv
import lxml.html

# Define the XPaths for the titles in the "Highlights" section
highlight_title_xpaths = [
    "/html/body/div/div[2]/main/section/div[1]/section[1]/div[1]/h2",
    "/html/body/div/div[2]/main/section/div[1]/section[1]/div[1]/ol/li/div/article/h3/a"
]

# Load the HTML file
with open('downloaded_pages/nytimes.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a parsed tree from the HTML content
tree = lxml.html.fromstring(html_content)

# Scrape and store the titles of the articles in the "Highlights" section
titles = []
for xpath in highlight_title_xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        title = element.text_content().strip()
        titles.append(title)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerows([[title] for title in titles])