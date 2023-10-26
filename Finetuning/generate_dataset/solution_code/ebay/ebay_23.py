import csv
from lxml import html

# Define the XPath for the desired element
xpath = "/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[1]/div/span/div/div[61]/span"

# Load the HTML file
with open("downloaded_pages/ebay.html", "r", encoding="utf-8") as file:
    html_data = file.read()

# Parse the HTML
tree = html.fromstring(html_data)

# Extract the text using the XPath
text = tree.xpath(xpath)[0].text_content()

# Prepare the data to be saved in CSV format
data = [["Result"]]
data.append([text])

# Save the data to a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)