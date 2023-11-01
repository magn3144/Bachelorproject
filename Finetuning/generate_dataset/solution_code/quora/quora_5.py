import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv

# Define the target URL
base_url = 'https://www.quora.com'
url = urljoin(base_url, '/user_directory')

# Send a GET request to the target URL
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all user profiles on the page
profiles = soup.find_all('a', class_='user')

# Scrape user profiles and their respective interests
data = []
for profile in profiles:
    profile_url = urljoin(base_url, profile['href'])
    profile_response = requests.get(profile_url)
    profile_soup = BeautifulSoup(profile_response.content, 'html.parser')
    user_name = profile_soup.find('span', class_='user_name').text.strip()
    user_interests = profile_soup.find_all('a', class_='topic_name')
    interests = [interest.text.strip() for interest in user_interests]
    data.append((user_name, interests))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['User', 'Interests'])
    writer.writerows(data)