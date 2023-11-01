import csv
import os
from pathlib import Path
from typing import List

from lxml import etree


def get_element_text(root: etree._Element, xpath: str) -> str:
    element = root.xpath(xpath)[0]
    return element.text.strip() if element.text else ""


def get_latest_post_titles_and_categories(html_path: str, category: str, elements: List[str], xpaths: List[str]):
    with open(html_path, "rb") as file:
        html = file.read()

    parser = etree.HTMLParser()
    root = etree.fromstring(html, parser)

    latest_posts = root.xpath('//div[@class="latest-posts"]')[0]
    
    post_titles = latest_posts.xpath('//div[@class="post-title"]')
    post_categories = latest_posts.xpath('//div[@class="post-category"]')

    data = []
    for title, category in zip(post_titles, post_categories):
        post_title = title.text.strip() if title.text else ""
        post_category = category.text.strip() if category.text else ""
        data.append([post_title, post_category])

    save_data_as_csv(data)


def save_data_as_csv(data: List[List[str]]):
    script_dir = Path(__file__).parent.resolve()
    output_file = os.path.join(script_dir, "scraped_data.csv")

    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Category"])
        writer.writerows(data)


if __name__ == "__main__":
    elements = ["<div class='post-title'>Sample Title 1</div>", "<div class='post-category'>Category 1</div>",
                "<div class='post-title'>Sample Title 2</div>", "<div class='post-category'>Category 2</div>",
                "<div class='post-title'>Sample Title 3</div>", "<div class='post-category'>Category 3</div>"]

    xpaths = [
        "//div[@class='post-title'][1]",
        "//div[@class='post-category'][1]",
        "//div[@class='post-title'][2]",
        "//div[@class='post-category'][2]",
        "//div[@class='post-title'][3]",
        "//div[@class='post-category'][3]"
    ]

    html_path = "downloaded_pages/techasoft.html"
    category = "Forums and Review Sites"

    get_latest_post_titles_and_categories(html_path, category, elements, xpaths)