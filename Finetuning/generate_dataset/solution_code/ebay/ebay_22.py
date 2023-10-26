import csv
from lxml import html

def extract_text(element, xpath):
    return element.xpath(xpath)[0].text_content()

def scrape_data():
    html_file = "downloaded_pages/ebay.html"
    category = "E-commerce"
    task = "Extract the text for 'Croatia, Republic of'"
    
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    tree = html.fromstring(content)
    
    data = {
        "Category": category,
        "Task": task,
        "Text": extract_text(tree, "/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[1]/div/span/div/div[51]/span")
    }
    
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

scrape_data()