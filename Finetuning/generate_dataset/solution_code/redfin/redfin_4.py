import csv
from lxml import html

def scrape_data():
    # Load the HTML file
    with open('downloaded_pages/redfin.html', 'r') as file:
        content = file.read()

    # Parse the HTML content
    tree = html.fromstring(content)

    # Extract property statistics
    property_stats = []
    property_elements = tree.xpath('//div[@class="stats"]')
    
    for element in property_elements:
        property_stats.append(element.text_content())

    # Save data to CSV file
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Property Statistics'])
        writer.writerows([(stat,) for stat in property_stats])

if __name__ == "__main__":
    scrape_data()