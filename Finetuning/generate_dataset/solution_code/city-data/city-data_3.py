import csv
from lxml import html

# Read the HTML file
with open("downloaded_pages/city-data.html", "r") as file:
    html_content = file.read()

# Create an ElementTree from the HTML content
tree = html.fromstring(html_content)

# Find the desired element using XPath
element = tree.xpath("/html/body/div[1]/div/div/div[2]/ul/li[6]/ul/table/tbody/tr[2]/td[4]/a")[0]

# Extract the text from the element
text = element.text_content()

# Write the scraped data to a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([text])