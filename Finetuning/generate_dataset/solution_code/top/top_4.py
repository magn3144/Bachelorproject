from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open("downloaded_pages/top.html", "r") as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Find the target <span> element
span_element = soup.find("span", class_="chakra-text css-1437ops")

# Extract the text
text = span_element.get_text()

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([text])