import csv
from lxml import etree

# XPaths for the HTML elements
xpath_fortune = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/ul/li[4]/div/div/div/div[2]/div"

# Function to extract text from an element using XPath
def extract_text(element, xpath):
    try:
        return element.xpath(xpath)[0].text.strip()
    except IndexError:
        return ""

# Read the HTML file
with open("downloaded_pages/finance.yahoo.html", "r") as file:
    html_content = file.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Extract the fortune text
fortune_text = extract_text(html_tree, xpath_fortune)

# Save the data as CSV
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Fortune"])
    writer.writerow([fortune_text])