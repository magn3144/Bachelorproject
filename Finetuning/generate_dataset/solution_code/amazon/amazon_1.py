import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/amazon.com.html', 'r') as file:
    html_data = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_data, 'html.parser')

# Find all the review elements
reviews = soup.find_all(class_='review')

# Create a CSV file to save the scraped data
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Review', 'Rating', 'Date'])

    # Extract the relevant information from each review element
    for review in reviews:
        review_text = review.find(class_='review-text').get_text().strip()
        rating = review.find(class_='review-rating').get_text().strip()
        date = review.find(class_='review-date').get_text().strip()
        writer.writerow([review_text, rating, date])