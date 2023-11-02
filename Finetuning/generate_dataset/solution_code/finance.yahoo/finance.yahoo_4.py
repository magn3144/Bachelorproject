import csv
from html.parser import HTMLParser


class YahooFinanceHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag

    def handle_data(self, data):
        if self.current_tag == 'p':
            self.data.append(data.strip())

    def reset(self):
        super().reset()
        self.data = []
        self.current_tag = None


def scrape_yahoo_finance_news(html_path):
    with open(html_path, 'r') as html_file:
        html_content = html_file.read()

    parser = YahooFinanceHTMLParser()
    parser.feed(html_content)

    return parser.data


def save_data_as_csv(data):
    with open('scraped_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for item in data:
            writer.writerow([item])


if __name__ == '__main__':
    scraped_data = scrape_yahoo_finance_news('downloaded_pages/finance.yahoo.html')
    save_data_as_csv(scraped_data)