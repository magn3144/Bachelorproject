import csv
from lxml import etree

def scrape_policy_info():
    # Load the HTML file
    with open('downloaded_pages/boardgamegeek.html', 'r') as f:
        html_content = f.read()

    # Parse the HTML content
    parser = etree.HTMLParser()
    tree = etree.fromstring(html_content, parser)

    # Find all footer links
    footer_links = tree.xpath('//div[@class="gg-footer-links"]/a')

    # Extract policy information from footer links
    policy_info = []
    for link in footer_links:
        policy_title = link.text.strip()
        policy_link = link.get('href')
        policy_info.append((policy_title, policy_link))

    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Policy Title', 'Policy Link'])
        writer.writerows(policy_info)

# Call the function to execute the scraping task
scrape_policy_info()