import csv
from lxml import etree

def extract_rating_details():
    html_path = 'downloaded_pages/bestbuy.html'
    target_category = 'E-commerce'
    target_elements = {
        'title': '/html/head/title',
        'product_title': '/html/body/div[4]/main/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[6]/div/div[4]/ol/li/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/ul/li/div/a/div/span',
        'rating': '/html/body/div[4]/main/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[6]/div/div[4]/ol/li/div/div/div/div/div/div[4]/a/div/p'
    }

    scraped_data = []

    with open(html_path, 'r', encoding='utf-8') as file:
        html = file.read()
        html_tree = etree.HTML(html)

        title = html_tree.xpath(target_elements['title'])
        if title:
            title = title[0].text

        product_titles = html_tree.xpath(target_elements['product_title'])
        ratings = html_tree.xpath(target_elements['rating'])

        for i in range(len(product_titles)):
            product_title = product_titles[i].text if product_titles[i] else ''
            rating = ratings[i].text if ratings[i] else ''

            scraped_data.append([title, product_title, rating])

    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Category', 'Product Title', 'Rating'])
        writer.writerows(scraped_data)

extract_rating_details()