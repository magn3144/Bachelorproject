import csv
from html.parser import HTMLParser

class DiscountedPriceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.discounted_prices = []
    
    def handle_starttag(self, tag, attrs):
        if tag == "span":
            for attr in attrs:
                if attr[0] == "class" and "aeecde" in attr[1]:
                    self.discounted_prices.append(attr[1]) 

def scrape_discounted_prices(html_file):
    parser = DiscountedPriceParser()
    with open(html_file, "r") as f:
        parser.feed(f.read())
    return parser.discounted_prices

def save_to_csv(data):
    with open("scraped_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Discounted Prices"])
        writer.writerows([[price] for price in data])

if __name__ == "__main__":
    html_file = "downloaded_pages/h&m.html"
    discounted_prices = scrape_discounted_prices(html_file)
    save_to_csv(discounted_prices)