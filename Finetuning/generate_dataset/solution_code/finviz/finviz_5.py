import csv
from lxml import etree

def scrape_stock_changes():
    # Load HTML file
    with open('downloaded_pages/finviz.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Parse HTML
    tree = etree.HTML(html)

    # Extract stock changes
    stock_changes = tree.xpath('/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[10]/a/span/text()')

    # Save data to CSV file
    with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Stock Changes'])
        for change in stock_changes:
            writer.writerow([change])

# Run the scraping function
scrape_stock_changes()