from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/trustpilot.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Extract the category names
categories = soup.find_all('a', class_='categories-list_category-link__1OVdy')
category_names = [category.text.strip() for category in categories]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category'])
    writer.writerows(zip(category_names))