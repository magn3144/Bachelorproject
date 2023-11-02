import csv
from pathlib import Path
from bs4 import BeautifulSoup

# Load HTML file
html_file = Path("downloaded_pages/washingtonpost.html")
with open(html_file, "r", encoding="utf-8") as file:
    html = file.read()

# Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Find all article titles and summaries
articles = soup.find_all("article")
data = []
for article in articles:
    title = article.find("h3").get_text(strip=True)
    summary = article.find("p").get_text(strip=True)
    data.append({"Title": title, "Summary": summary})

# Save data as CSV
csv_file = "scraped_data.csv"
fieldnames = ["Title", "Summary"]
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)