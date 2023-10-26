import csv
from lxml import etree

def extract_data(html_file):
    with open(html_file, 'r') as file:
        html_data = file.read()
    root = etree.HTML(html_data)
    
    latest_news_headlines = root.xpath('/html/body/div/div/main/div/section[2]/div/div[1]/div[1]/h1/span[2]/span')
    latest_news_descriptions = root.xpath('/html/body/div/div/main/div/section[2]/div/div[2]/div[1]/div/a/div/div/div[2]/div/p')

    data = []
    for i in range(len(latest_news_headlines)):
        headline = latest_news_headlines[i].text
        description = latest_news_descriptions[i].text
        data.append([headline, description])
        
    return data

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Headline', 'Description'])
        writer.writerows(data)

html_file = 'downloaded_pages/fifa.html'
data = extract_data(html_file)
save_to_csv(data)