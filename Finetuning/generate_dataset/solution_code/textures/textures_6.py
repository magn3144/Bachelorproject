import csv
from lxml import html

# Define the URLs and XPaths
page_url = 'file:///downloaded_pages/textures.html'
download_count_xpath = '//div[@class="download-count"]/text()'

# Scrape download counts
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Download Count'])

    # Parse the HTML
    page = html.parse(page_url)
    download_counts = page.xpath(download_count_xpath)

    # Write download counts to CSV
    for count in download_counts:
        writer.writerow([count])
