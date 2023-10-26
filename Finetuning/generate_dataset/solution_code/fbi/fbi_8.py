import csv
from lxml import html

def scrape_data():
    tree = html.parse("downloaded_pages/fbi.html")

    category_names = tree.xpath("//div[@class='content']//ul/li[position()=5]//a/text()")
    category_links = tree.xpath("//div[@class='content']//ul/li[position()=5]//a/@href")

    scraped_data = []
    for name, link in zip(category_names, category_links):
        scraped_data.append([name, link])

    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Link"])  # Header
        writer.writerows(scraped_data)

if __name__ == "__main__":
    scrape_data()