import csv
from lxml import etree
from urllib.parse import urljoin


def scrape_website(category, webpage, xpath_elements):
    try:
        parser = etree.HTMLParser()
        tree = etree.parse(webpage, parser)
        url = tree.getroot()

        video_titles = []
        video_links = []

        for xpath, element in xpath_elements.items():
            results = url.xpath(xpath)
            if results:
                if element == 'a':
                    for result in results:
                        video_title = result.text.strip()
                        video_link = urljoin(webpage, result.get('href'))
                        video_titles.append(video_title)
                        video_links.append(video_link)

        scraped_data = list(zip(video_titles, video_links))

        headers = ['Title', 'Link']
        with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(scraped_data)

        print('Scraping completed successfully!')
        return True

    except Exception as e:
        print(f'Scraping failed due to error: {e}')
        return False


category = 'Sports Websites'
webpage = 'downloaded_pages/espn.html'

xpath_elements = {
    "/html/body/div[1]/div/div/div/main/div[3]/div/div[2]/div/section[2]/div[2]/div/div[2]/div/a/div/div/span": 'span',
    "/html/body/div[1]/div/div/div/main/div[3]/div/div[2]/div/aside[2]/section/div/div/div[2]/a/div/h2": 'h2',
    "/html/body/div[1]/div/div/div/main/div[3]/div/div[2]/div/aside[2]/section/div/div/div[2]/a/@href": 'a'
}

scrape_website(category, webpage, xpath_elements)