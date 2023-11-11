import csv
from lxml import html

def get_distance(element):
    distance = element.text.strip().split()[0]
    return distance

def save_as_csv(data):
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Property', 'Distance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def scrape_html():
    tree = html.parse('downloaded_pages/booking.html')
    data = []
    
    properties = tree.xpath('//div[@class="aee5343fdb def9bc142a"]')
    distances = tree.xpath('//h3[contains(@class, "a3332d346a e6208ee469 d0caee4251")][contains(text(), "Distance from centre")]/following-sibling::span')
    
    for prop, dist in zip(properties, distances):
        prop_name = prop.text.strip()
        prop_dist = get_distance(dist)
        data.append({'Property': prop_name, 'Distance': prop_dist})
    
    save_as_csv(data)

scrape_html()