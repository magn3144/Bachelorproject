import csv
from lxml import etree

def save_data_as_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title'])
        writer.writerows(data)

def get_titles(html_path):
    tree = etree.parse(html_path)
    root = tree.getroot()
    
    news_articles = root.xpath('//div[@class="category" and text()="NEWS"]/ancestor::article')
    
    titles = []
    for article in news_articles:
        title_element = article.xpath('.//h4[@class="description"]')
        if title_element:
            title = title_element[0].text.strip()
            titles.append([title])
    
    return titles

html_path = 'downloaded_pages/myspace.html'
titles = get_titles(html_path)
save_data_as_csv(titles)