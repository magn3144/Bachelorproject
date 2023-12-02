
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the elements containing the duration
durations = tree.xpath('//span[@class="ipc-rating-star--voteCount"]')

# Collect the durations
data = []
for duration in durations:
    duration = duration.text.strip()
    data.append([duration])

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Duration'])
    writer.writerows(data)
