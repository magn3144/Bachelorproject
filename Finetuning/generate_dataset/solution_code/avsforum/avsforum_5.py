import csv
from lxml import html

# Define the HTML elements and their corresponding XPaths
html_elements = {
    "banner_text": [
        '<p>Enjoy banner ad-free browsing with AVS Forum Plus</p>',
        '/html/body/div[1]/div[4]/div/div/div/div/div/div[2]/aside/p'
    ]
}

# Parse the HTML file
with open("downloaded_pages/avsforum.html", "r") as f:
    page_content = f.read()
tree = html.fromstring(page_content)

# Retrieve the banner text using XPath
banner_text = tree.xpath(html_elements["banner_text"][1])[0].text_content().strip()

# Save the scraped data as a CSV file
data = [["Banner Text"], [banner_text]]
with open("scraped_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)