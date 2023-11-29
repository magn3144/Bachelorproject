import csv
from bs4 import BeautifulSoup

# Load the HTML data from local file.
with open('downloaded_pages/airbnb.html', 'r') as file:
    page_content = file.read().replace('\n', '')

# Get the text of all div elements with the class "t1jojoys dir dir-ltr"
soup = BeautifulSoup(page_content, 'html.parser')
divs = soup.find_all("div", {"class": "t1jojoys dir dir-ltr"})
divs_text = [div.text for div in divs]

# Get the text of all span elements with the class "dir dir-ltr"
soup = BeautifulSoup(page_content, 'html.parser')
spans = soup.find_all("span", {"class": "_tyxjp1"})
spans_text = [span.text for span in spans]
# Remove empty strings from the list
spans_text = list(filter(None, spans_text))
# Remove dates containing "–" from the list
spans_text = [span for span in spans_text if "DKK" in span]

# Save the data to a CSV file in two seperate columns.
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for div, span in zip(divs_text, spans_text):
        writer.writerow([div, span])