import csv
from lxml import etree

def extract_dates(element):
    dates = element.xpath('//div[contains(@class, "usajobs-search-result--core__dates")]')
    opening_closing_dates = []
    for date in dates:
        opening = date.xpath('.//span[@class="opening-date"]/text()')
        closing = date.xpath('.//span[@class="closing-date"]/text()')
        if opening and closing:
            opening_closing_dates.append([opening[0].strip(), closing[0].strip()])
    return opening_closing_dates

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Opening Date', 'Closing Date'])
        writer.writerows(data)

# Load the HTML file
with open('downloaded_pages/usajobs.html', 'r') as html_file:
    html = html_file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Scrape the opening and closing dates
dates = extract_dates(tree)

# Save the scraped data as CSV
save_to_csv(dates)