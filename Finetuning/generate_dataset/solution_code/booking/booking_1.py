import csv
from lxml import etree

def extract_location_and_rating():
    # Load the HTML file
    html_file = "downloaded_pages/booking.html"
    with open(html_file, "r", encoding="utf-8") as file:
        html = file.read()

    # Parse the HTML
    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

    # Find all property elements
    property_elements = tree.xpath("//div[contains(@class,'sr_item')]")
    
    # Prepare CSV file
    csv_file = "scraped_data.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Location", "Rating"])

        # Extract location and rating for each property
        for property_element in property_elements:
            location = property_element.xpath(".//span[contains(@class,'aee5343fdb')]/text()")[0].strip()
            rating_element = property_element.xpath(".//div[contains(@class,'review-score-badge')]/text()")[0]
            rating = rating_element.strip() if rating_element else "N/A"

            writer.writerow([location, rating])

    print("Scraping completed. Data saved in 'scraped_data.csv'")

# Run the function
extract_location_and_rating()