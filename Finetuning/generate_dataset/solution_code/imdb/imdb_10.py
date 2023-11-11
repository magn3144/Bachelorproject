import csv
from lxml import html

def scrape_movies():
    # Open the HTML file
    with open('downloaded_pages/imdb.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Parse the HTML content
    tree = html.fromstring(html_content)

    # Retrieve the titles and release years of the movies
    movie_titles = tree.xpath('//div[@class="ipc-title__text"]/text()')
    movie_release_years = tree.xpath('//span[@class="sc-c7e5f54-8 fiTXuB cli-title-metadata-item"]/text()')

    # Define the range of positions
    start_position = 55
    end_position = 66

    # Slice the movie titles and release years based on the range of positions
    movie_titles_range = movie_titles[start_position-1:end_position]
    movie_release_years_range = movie_release_years[start_position-1:end_position]

    # Create a list of dictionaries for each movie
    movie_data = []
    for title, release_year in zip(movie_titles_range, movie_release_years_range):
        movie_data.append({'Title': title, 'Release Year': release_year})

    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Release Year']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(movie_data)

# Call the function to scrape the movies and save the data as a CSV file
scrape_movies()