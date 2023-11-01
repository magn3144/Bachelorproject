import csv
from bs4 import BeautifulSoup

# Load the HTML file
html_file = "downloaded_pages/google news.html"
with open(html_file, "r") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all the <h4> tags with class "JtKRv iTin5e"
h4_tags = soup.find_all("h4", class_="JtKRv iTin5e")

# Extract the text and corresponding XPaths
data = []
for h4 in h4_tags:
    text = h4.get_text()
    xpath = soup.find_parent().find_all(recursive=False).index(h4)
    data.append((text, xpath))

# Save the scraped data as a CSV file
csv_file = "scraped_data.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Text", "XPath"])
    writer.writerows(data)