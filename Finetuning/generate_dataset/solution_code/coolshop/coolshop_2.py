import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open("downloaded_pages/coolshop.html", "r") as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find the recommended categories elements
recommended_categories = soup.find_all("h2", class_="cpn-recommended-products__title")

# Extract the titles of the recommended categories
titles = [category.get_text() for category in recommended_categories]

# Save the data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Recommended Category Titles"])
    writer.writerows([[title] for title in titles])