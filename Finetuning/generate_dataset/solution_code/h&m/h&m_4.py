import csv
from lxml import html

# Define the local path to the HTML file
html_path = "downloaded_pages/h&m.html"

# Define the XPaths for the elements to scrape
legend_xpath = "/html/body/div/div[3]/main/div[2]/div[1]/div/div/div/form/legend"

# Load the HTML file
with open(html_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Scrape the legend tag
legend_element = tree.xpath(legend_xpath)[0]
legend_text = legend_element.text_content()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Legend Text'])
    writer.writerow([legend_text])