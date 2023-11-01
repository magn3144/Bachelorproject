import csv
from lxml import html

# Define the web page file path and category
web_page = "downloaded_pages/tripadvisor.html"
category = "Forums and Review Sites"

def scrape_restaurants_with_outdoor_seating():
    # Open the web page file and parse it using lxml
    with open(web_page, "r", encoding="utf-8") as file:
        page_content = file.read()
    tree = html.fromstring(page_content)

    # Find all div elements with the class "biGQs _P pZUbB KxBGd" (restaurants with outdoor seating)
    restaurant_divs = tree.xpath("//div[@class='biGQs _P pZUbB KxBGd']")

    # Create a list to store the scraped data
    scraped_data = []

    # Iterate over the restaurant divs and extract the restaurant name
    for restaurant_div in restaurant_divs:
        restaurant_name = restaurant_div.text.strip()
        scraped_data.append(restaurant_name)

    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Restaurant Name"])
        writer.writerows(zip(scraped_data))

# Run the scraping function
scrape_restaurants_with_outdoor_seating()