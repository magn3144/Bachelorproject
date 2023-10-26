import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/cnn.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the ad feedback submitted message
ad_feedback_message = soup.find('div', class_='ad-feedback__submitted__message').get_text(strip=True)

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Ad Feedback Submitted Message'])
    writer.writerow([ad_feedback_message])