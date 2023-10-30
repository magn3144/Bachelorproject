from bs4 import BeautifulSoup
import csv

# Local path to the HTML file
html_file_path = "downloaded_pages/bog & ide.html"

# XPaths of the HTML elements
xpaths = {
    "title": "/html/body/div/main/div[1]/div[2]/div/section[4]/div[2]/div/div/div/div[12]/div/a/span"
}

# Create a BeautifulSoup object with the HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract the book title using the XPath
title = soup.find("span", xpath=xpaths["title"]).text

# Save the scraped data as a CSV file
data = [["Book Title"], [title]]
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)