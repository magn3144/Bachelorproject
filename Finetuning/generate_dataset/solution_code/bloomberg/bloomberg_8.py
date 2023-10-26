import csv
from lxml import etree

# Define the XPath expressions for the required elements
category_xpath = "/html/body/div[1]/div[2]/div[2]/div[2]/nav/div[2]/ul/li[2]/ul/li[8]/div/div[3]/section/h2"
headlines_xpath = "/html/body/div[1]/div[2]/div[2]/div[2]/nav/div[2]/ul/li[2]/ul/li[8]/div/section[1]/article/div[2]/a/h3[contains(text(), 'Crypto')]"

# Load the HTML file
with open("downloaded_pages/bloomberg.html", "rb") as f:
    html = f.read()

# Parse the HTML content
tree = etree.HTML(html)

# Extract the category
category_element = tree.xpath(category_xpath)[0]
category = category_element.text.strip()

# Extract the headlines
headlines_elements = tree.xpath(headlines_xpath)
headlines = [element.text.strip() for element in headlines_elements]

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Category", "Headline"])
    writer.writerow([category, ""])  # Leave a blank row for the category
    for headline in headlines:
        writer.writerow(["", headline])  # Leave a blank row for each headline