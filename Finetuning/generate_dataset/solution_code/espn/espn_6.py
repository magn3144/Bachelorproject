import csv
from bs4 import BeautifulSoup

# Path to the HTML file
html_path = 'downloaded_pages/espn.html'

# HTML elements containing video descriptions
video_description_elements = [
    'p.vjs-modal-dialog-description',
    'div.News__Item__Description',
    'div.MediaList__item__description',
]

# Retrieve video descriptions from the HTML file
video_descriptions = []
with open(html_path, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    for element in video_description_elements:
        descriptions = soup.select(element)
        for description in descriptions:
            video_descriptions.append(description.text.strip())

# Save video descriptions as CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for description in video_descriptions:
        writer.writerow([description])