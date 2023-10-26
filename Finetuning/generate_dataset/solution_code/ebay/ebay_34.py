import csv
from lxml import html

def scrape_data():
    # Read the HTML file
    with open('downloaded_pages/ebay.html', 'r', encoding='utf-8') as file:
        page_content = file.read()

    # Parse the HTML
    tree = html.fromstring(page_content)

    # Extract the desired text using XPath
    text = tree.xpath('/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[1]/div/span/div/div[40]/span/text()')

    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Scraped Text'])
        writer.writerow([text])

# Call the function to start the scraping process
scrape_data()