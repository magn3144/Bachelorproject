import csv
import os
from lxml import html

def get_ratings():
    # Load the html file
    with open('downloaded_pages/imdb.html', 'r') as file:
        page_content = file.read()

    # Parse the html content
    parsed_content = html.fromstring(page_content)

    # Get the ratings
    ratings = parsed_content.xpath('//div[@class="ipc-star INTEGER"]/text()')

    # Return the ratings
    return ratings


def save_csv(data):
    # Prepare csv file
    filename = 'scraped_data.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['User Ratings'])
        for row in data:
            writer.writerow(row)


def main():
    # Get ratings
    data = get_ratings()

    # Save as csv
    save_csv(data)


if __name__ == '__main__':
    main()