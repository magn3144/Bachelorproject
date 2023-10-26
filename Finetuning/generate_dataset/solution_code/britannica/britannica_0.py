from bs4 import BeautifulSoup
import csv

# Load the HTML file
file_path = 'downloaded_pages/britannica.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all email labels in the footer
email_labels = soup.select('footer label.sr-only')

# Prepare data for CSV file
data = [['Email Label']]
for label in email_labels:
    data.append([label.text.strip()])

# Save data as a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)