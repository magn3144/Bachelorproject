import csv
from bs4 import BeautifulSoup


def extract_email_subscription_text(html_file):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        elements = soup.find_all('p', class_='uscb-email-subscription-text')
        subscription_text = [element.text.strip() for element in elements]

    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Email Subscription Text'])
        for text in subscription_text:
            writer.writerow([text])


html_file = 'downloaded_pages/census.html'
extract_email_subscription_text(html_file)