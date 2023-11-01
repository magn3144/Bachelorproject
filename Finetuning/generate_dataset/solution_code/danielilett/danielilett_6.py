import csv
from bs4 import BeautifulSoup


def scrape_navigation_links(html_file_path):
    with open(html_file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        nav_links = soup.find_all(class_='navlinks-parent')

        scraped_data = []
        for link in nav_links:
            link_text = link.text.strip()
            link_xpath = link.parent['xpath']
            scraped_data.append([link_text, link_xpath])

    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Link Text', 'XPath'])
        writer.writerows(scraped_data)


scrape_navigation_links('downloaded_pages/danielilett.html')