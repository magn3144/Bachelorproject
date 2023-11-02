import csv
from lxml import html

# Path to the HTML file
path = "downloaded_pages/finance.yahoo.html"

# XPaths of the notifications
xpaths = [
    "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/div[2]/ul/li[29]/a/div/div/p",
    "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/div[2]/ul/li[34]/a/div/div/p",
    "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/div[2]/h4"
]

# List to store the scraped notifications
notifications = []

# Parse the HTML file
with open(path, "r") as file:
    content = file.read()
    tree = html.fromstring(content)

# Scrape the notifications using the XPaths
for xpath in xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        notification = element.text.strip()
        notifications.append(notification)

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Notifications"])
    writer.writerows([[notification] for notification in notifications])