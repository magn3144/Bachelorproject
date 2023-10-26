import csv
from lxml import html

def extract_category(tree):
    category_path = "/html/body/div[8]/header/div[1]/div/div/h2"
    category_element = tree.xpath(category_path)
    if category_element:
        return category_element[0].text
    else:
        return None

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Category"])
        for category in data:
            writer.writerow([category])

def main():
    file_path = "downloaded_pages/bbc.html"
    with open(file_path, "r", encoding="utf-8") as file:
        page_content = file.read()
    tree = html.fromstring(page_content)
    category = extract_category(tree)
    if category:
        save_to_csv([category])

if __name__ == "__main__":
    main()