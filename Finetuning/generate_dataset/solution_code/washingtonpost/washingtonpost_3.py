import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open("downloaded_pages/washingtonpost.html", "r") as f:
    html = f.read()

# Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Find all the image captions
image_captions = []
for img in soup.find_all("img"):
    caption = img.get("alt", "")
    if caption:
        image_captions.append(caption)

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Image Caption"])
    writer.writerows(zip(image_captions))