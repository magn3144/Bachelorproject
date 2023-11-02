from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/census.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the email subscription text
email_subscription_text = soup.find('p', class_='uscb-email-subscription-text').text.strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Email Subscription Text'])
    writer.writerow([email_subscription_text])