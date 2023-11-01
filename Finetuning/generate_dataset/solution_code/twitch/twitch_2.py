import csv
from lxml import html

# Function to scrape the data
def scrape_data():
    # Open the HTML file
    with open('downloaded_pages/twitch.html', 'r', encoding='utf-8') as file:
        page_content = file.read()

    # Parse the HTML
    parsed_page = html.fromstring(page_content)

    # Get all article headlines
    headlines = parsed_page.xpath('//h2[@class="article-headline"]//text()')

    # Get all publication dates
    dates = parsed_page.xpath('//div[@class="article-meta"]/span[@class="date"]/text()')

    # Combine headlines and dates into a list of tuples
    data = list(zip(headlines, dates))

    # Save the data in a CSV file
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Headline', 'Publication Date'])  # Header row
        writer.writerows(data)

# Call the scrape_data function
scrape_data()