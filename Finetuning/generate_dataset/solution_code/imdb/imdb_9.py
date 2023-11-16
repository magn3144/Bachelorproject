import csv
import lxml.html

def write_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def scrape_selectable(html_file_path):
    with open(html_file_path, 'r') as f:
        tree = lxml.html.fromstring(f.read())
    
    data = []
    labels = tree.xpath('.//*[self::label or self::span or self::div or self::a or self::h3 or self::p or self::li or self::title]')
    
    for label in labels:
        if 'class' in label.attrib:
            class_value = label.attrib['class'].split(' ')
            for value in class_value:
                if "select" in value or "option" in value or "link" in value:
                    data.append({"text": label.text})
                else:
                    continue
        else:
            continue
            
    return data

if __name__ == "__main__":
    html_file_path = 'downloaded_pages/imdb.html'
    data = scrape_selectable(html_file_path)
    write_to_csv(data, 'scraped_data.csv')