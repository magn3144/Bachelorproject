import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open("downloaded_pages/seekingalpha.html", "r") as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find all article links on the 'Market News' page
article_links = soup.select("h1:contains('Market News') + div a")

# Save the scraped data in a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Article Link"])
    for link in article_links:
        writer.writerow([link["href"]])