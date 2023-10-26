import csv
from lxml import etree

# Define the local path to the HTML file
html_file_path = "downloaded_pages/avsforum.html"

# Define the XPath for the target element
target_xpath = "/html/body/div[1]/footer/div/div[1]/div[1]/div/ul/li[6]/a"

# Parse the HTML file
with open(html_file_path, "r") as f:
    html = f.read()
tree = etree.HTML(html)

# Extract the text from the target element
target_element = tree.xpath(target_xpath)[0]
text = target_element.text.strip()

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([text])