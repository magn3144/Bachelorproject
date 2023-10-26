import csv
from lxml import html

def scrape_website():
    # Open the HTML file
    with open('downloaded_pages/city-data.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Create an ElementTree object from the HTML content
    tree = html.fromstring(html_content)

    # Extract the text from the <a> element with XPath /html/body/div[3]/div[4]/div[14]/div/a[2]
    xpath = '/html/body/div[3]/div[4]/div[14]/div/a[2]'
    elements = tree.xpath(xpath)
    scraped_data = [element.text for element in elements]

    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Scraped Data'])  # Write header
        writer.writerows([[data] for data in scraped_data])

# Run the scraping function
scrape_website()