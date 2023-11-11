import requests
from lxml import html
import csv

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as file:
    html_content = file.read()

# Create an lxml tree from the HTML content
tree = html.fromstring(html_content)

# Define the XPath expressions for the required movie details
movie_titles_xpath = [
    '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[136]/div[2]/div/div/div[1]/a/h3',
    '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[154]/div[2]/div/div/div[1]/a/h3',
    '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[228]/div[2]/div/div/div[1]/a/h3'
]

release_years_xpath = [
    '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[136]/div[2]/div/div/div[2]/span[1]',
    '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[154]/div[2]/div/div/div[2]/span[1]',
    '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[228]/div[2]/div/div/div[2]/span[1]'
]

ratings_xpath = [
    '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[136]/div[2]/div/div/span/div/span/span',
    '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[154]/div[2]/div/div/span/div/span/span',
    '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[228]/div[2]/div/div/span/div/span/span'
]

# Extract the movie details
movie_titles = [tree.xpath(xpath)[0].text_content() for xpath in movie_titles_xpath]
release_years = [tree.xpath(xpath)[0].text_content() for xpath in release_years_xpath]
ratings = [tree.xpath(xpath)[0].text_content() for xpath in ratings_xpath]

# Combine the movie details
movie_details = zip(movie_titles, release_years, ratings)

# Save the movie details as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Release Year', 'Rating'])
    writer.writerows(movie_details)