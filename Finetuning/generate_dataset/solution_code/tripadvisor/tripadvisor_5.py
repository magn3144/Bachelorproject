import csv
from lxml import html

def scrape_romantic_restaurants():
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Restaurant Name', 'Category', 'Rating'])
        
        tree = html.parse('downloaded_pages/tripadvisor.html')
        
        romantic_restaurants = tree.xpath('//a[contains(@class, "cJTqz") and contains(text(), "Romantiske restauranter")]')
        
        for restaurant in romantic_restaurants:
            name = restaurant.text
            category = 'Romantic'
            rating = restaurant.xpath('../../span[contains(@class, "YECgr")]')[0].text
            writer.writerow([name, category, rating])

scrape_romantic_restaurants()