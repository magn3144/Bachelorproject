import csv
from lxml import etree
from io import StringIO

def extract_title(html_content):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html_content), parser)
    title_element = tree.xpath("/html/head/title")[0]
    return title_element.text

def save_to_csv(data):
    with open('scraped_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title'])
        writer.writerow([data])

def main():
    with open('downloaded_pages/jysk.html', 'r') as file:
        html_content = file.read()
        title = extract_title(html_content)
        save_to_csv(title)

if __name__ == "__main__":
    main()