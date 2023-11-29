import csv
from bs4 import BeautifulSoup

# Load the HTML data from local file.
with open('downloaded_pages/airbnb.html', 'r') as file:
    page_content = file.read().replace('\n', '')

# Get the text of all span elements with the class "dir dir-ltr"
soup = BeautifulSoup(page_content, 'html.parser')
spans = soup.find_all("span", {"class": "dir dir-ltr"})
spans_text = [span.text for span in spans]
# Remove dates containing "–" from the list
spans_text = [span for span in spans_text if "–" in span]

# Save the data to a CSV file.
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for span in spans_text:
        writer.writerow([span])