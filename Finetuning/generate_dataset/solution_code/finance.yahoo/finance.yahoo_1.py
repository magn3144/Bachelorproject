import csv
from lxml import etree

# Load the HTML file
html_file = "downloaded_pages/finance.yahoo.html"
with open(html_file, "r", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.HTML(html)

# Find the options with highest implied volatility
options_xpath = "/html/body/div[1]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/ul/li[13]/a"
options = tree.xpath(options_xpath)

# Extract the text from the options
options_text = [option.text for option in options]

# Save the scraped data as a CSV file
csv_file = "scraped_data.csv"
with open(csv_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Options with Highest Implied Volatility"])
    writer.writerows([[option] for option in options_text])