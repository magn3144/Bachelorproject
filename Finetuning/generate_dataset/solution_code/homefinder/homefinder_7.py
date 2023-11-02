import csv
from lxml import html

# Define the local path to the HTML file
path_to_html = "downloaded_pages/homefinder.html"

# Read the HTML file
with open(path_to_html, 'r') as f:
    html_content = f.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract the search title
search_title_xpath = '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[1]/div/div[1]/h1'
search_title_element = tree.xpath(search_title_xpath)

# Get the text from the search title element
search_title = search_title_element[0].text_content() if search_title_element else ""

# Save the search title as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([search_title])