import csv
from bs4 import BeautifulSoup

# Open the HTML file and parse it using BeautifulSoup
with open("downloaded_pages/aljazeera.html", "r") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# Find all sibling and linked sites
sibling_sites = soup.find_all("span", class_="screen-reader-text")

# Write the data to a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Sibling Sites"])

    for site in sibling_sites:
        writer.writerow([site.text])