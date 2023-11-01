import csv
from lxml import etree

# define the HTML elements and their corresponding XPaths
elements = {
    'review': '//div[@class="review"]',
    'rating': '//span[@class="rating"]'
}

# open the HTML file
with open('downloaded_pages/normal.html', 'r') as file:
    html = file.read()

# create an empty list to store the scraped data
data = []

# parse the HTML
tree = etree.HTML(html)

# retrieve all customer reviews and ratings
reviews = tree.xpath(elements['review'])
ratings = tree.xpath(elements['rating'])

# loop through the reviews and retrieve the text and rating
for review, rating in zip(reviews, ratings):
    review_text = review.text.strip() if review.text else ''
    rating_text = rating.text.strip() if rating.text else ''
    data.append([review_text, rating_text])

# save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Review', 'Rating'])
    writer.writerows(data)