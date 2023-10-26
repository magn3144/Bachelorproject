from typing import List
import csv
from lxml import html


def extract_text(element) -> str:
    if element is not None:
        return element.text_content().strip()
    return ""


def scrape_market_news_page(html_file: str):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    tree = html.fromstring(content)

    news_summaries = []
    news_elements = tree.xpath("//h3[@class='m-0 inline-block text-5x-large-r text-black-35 dark:text-black-30 md:text-4x-large-r']")
    for element in news_elements:
        news_summaries.append(extract_text(element))

    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Summary'])
        for summary in news_summaries:
            writer.writerow([summary])


scrape_market_news_page('downloaded_pages/seekingalpha.html')