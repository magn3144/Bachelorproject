import csv
from bs4 import BeautifulSoup

# Load the HTML file
html_file_path = 'downloaded_pages/washingtonpost.html'
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all figcaption tags with the specified class
figcaption_tags = soup.find_all('figcaption', class_='gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs')

# Extract the text from the figcaption tags
captions_text = [tag.get_text(strip=True) for tag in figcaption_tags]

# Save the scraped data as a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])
    writer.writerows(zip(captions_text))