import csv
from lxml import html

def extract_dates():
    # Parse the HTML
    with open("downloaded_pages/airbnb.html", "r") as f:
        page_content = f.read()
        tree = html.fromstring(page_content)

    # Extract date elements
    dates_xpath = '/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[10]/div/div[2]/div/div/div/div/div/div[2]/div[3]/span/span'
    date_elements = tree.xpath(dates_xpath)

    # Extract text from elements
    dates = [date.text for date in date_elements]

    # Write dates to a CSV file
    with open('scraped_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date'])
        for date in dates:
            writer.writerow([date])

extract_dates()