import csv
from lxml import html

def extract_text_from_elements(elements):
    texts = []
    for element in elements:
        texts.append(element.text_content().strip())
    return texts

def save_as_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Text"])
        writer.writerows(data)

def main():
    html_file = 'downloaded_pages/employmentfirstfl.html'
    tree = html.parse(html_file)
    
    elements = tree.xpath('/html/body/div/footer/div[2]/p')
    texts = extract_text_from_elements(elements)
    
    save_as_csv(texts)

if __name__ == "__main__":
    main()