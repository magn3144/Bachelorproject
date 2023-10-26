from bs4 import BeautifulSoup
import csv

# Open the HTML file
html_path = "downloaded_pages/britannica.html"
with open(html_path, "r", encoding="utf-8") as file:
    html_content = file.read()
    
# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the articles explaining how dinosaurs became birds
article_headings = soup.find_all("h2", text="How Dinosaurs Became Birds")

# Create a list to store the scraped data
data = []
data.append(["Category", "Heading"])

# Extract the headings and add them to the data list
for heading in article_headings:
    data.append(["Educational Websites", heading.text])

# Save the data as a CSV file
csv_path = "scraped_data.csv"
with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)