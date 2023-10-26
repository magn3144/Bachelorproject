from lxml import etree
import csv

# Parse the HTML file
with open('downloaded_pages/seekingalpha.html', 'r') as file:
    html = file.read()
tree = etree.HTML(html)

# Find all article footers on the 'Market News' page
article_footers = tree.xpath('/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article/div/div/footer')

# Extract stock ticker symbols from article footers and save them in a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Stock Ticker'])
    
    for footer in article_footers:
        stock_ticker = footer.xpath('span[1]/a/span[1]/text()')
        writer.writerow(stock_ticker)