import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open("downloaded_pages/census.html", "r") as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, "html.parser")

# Find the target element
target_element = soup.find("a", class_="uscb-footer-link", text="Data Protection and Priva")

# Extract the text
target_text = target_element.text.strip()

# Write the scraped data to a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([target_text])