import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open("downloaded_pages/almanac.html", "r") as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, "html.parser")

# Find all the items listed in Yankee Magazine
items = soup.find_all("a", class_="menu__link--link menu__link--level-1")

# Extract the names and prices of the items
data = []
for item in items:
    name = item.text.strip()
    price = item.next_sibling.strip()
    data.append((name, price))

# Save the data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price"])
    writer.writerows(data)