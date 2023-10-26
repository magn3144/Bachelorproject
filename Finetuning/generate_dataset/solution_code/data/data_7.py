import csv
from lxml import html

# Read the HTML file
with open("downloaded_pages/data.cdc.html", "r") as f:
    page_content = f.read()

# Parse the HTML content
tree = html.fromstring(page_content)

# Extract the browse2-mobile-filter-content element
filter_content_element = tree.xpath("/html/body/div[2]/div/div[6]/div/div[4]/div[2]/div[2]/div[8]/div/div[2]/div[3]")[0]

# Extract the text from the element
filter_content_text = filter_content_element.text.strip()

# Save the extracted data as a CSV file
with open("scraped_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([filter_content_text])