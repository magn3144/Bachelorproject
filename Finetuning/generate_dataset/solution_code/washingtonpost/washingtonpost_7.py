import csv
from bs4 import BeautifulSoup

# Define the path to the HTML file
html_file_path = "downloaded_pages/washingtonpost.html"

# Initialize a list to store the scraped data
scraped_data = []

# Open the HTML file and create a BeautifulSoup object
with open(html_file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find all the <a> tags with the specified class and extract the text
a_tags = soup.find_all("a", class_="wpds-c-iifZmx wpds-c-iifZmx-gzQzMU-desktopVariant-true")
for a_tag in a_tags:
    scraped_data.append(a_tag.get_text())

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(scraped_data)