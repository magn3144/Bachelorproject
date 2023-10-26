import csv
from lxml import etree

# Load the HTML file and parse it
html_file = "downloaded_pages/amazon.html"
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Define the XPaths for the investor relations information
xpaths = [
    "/html/body/div[1]/div[3]/div[1]/div/div[1]/ul/li[4]/a",  # Investor Relations link
    "/html/body/div[1]/div[3]/div[1]/div/div[7]/ul/li[2]/a",  # Your Account link
    "/html/body/div[1]/div[3]/div[1]/div/div[7]/ul/li[4]/a",  # Shipping Rates & Policies link
    "/html/body/div[1]/div[3]/div[1]/div/div[5]/ul/li[1]/a",  # Amazon Business Card link
    "/html/body/div[1]/div[3]/div[1]/div/div[3]/ul/li[8]/a",  # See More Make Money with Us link
    "/html/body/div[1]/div[3]/div[1]/div/div[3]/ul/li[5]/a",  # Advertise Your Products link
]

# Initialize the scraped data list
scraped_data = []

# Scrape the investor relations information using the XPaths
for xpath in xpaths:
    elements = tree.xpath(xpath)
    if elements:
        text = elements[0].text.strip()
        scraped_data.append(text)
    else:
        scraped_data.append("N/A")

# Save the scraped data as a CSV file
csv_file = "scraped_data.csv"
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Investor Relations", "Your Account", "Shipping Rates & Policies",
                     "Amazon Business Card", "See More Make Money with Us", "Advertise Your Products"])
    writer.writerow(scraped_data)