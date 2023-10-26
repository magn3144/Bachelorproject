import csv
from lxml import etree

def scrape_text():
    # Open the HTML file and parse it
    with open('downloaded_pages/ebay.html', 'r', encoding='utf-8') as f:
        html = f.read()
    parser = etree.HTMLParser()
    tree = etree.HTML(html, parser)
    
    # Retrieve the text for "French Guiana"
    french_guiana_text = tree.xpath('/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[1]/div/span/div/div[69]/span/text()')[0].strip()

    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Category', 'Task', 'Scraped Text'])
        writer.writerow(['E-commerce', 'Retrieve text for "French Guiana"', french_guiana_text])

# Call the function to scrape text and save the data as CSV
scrape_text()