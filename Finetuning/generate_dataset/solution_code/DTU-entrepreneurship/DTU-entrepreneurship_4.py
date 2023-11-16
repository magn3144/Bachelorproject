import csv
from lxml import html as html_parser

def extract_validation_messages(file_path):
    with open(file_path, 'r') as html_file:
        source_code = html_file.read()
        
    html_tree = html_parser.fromstring(source_code)
    
    validation_messages_xpaths = [
        '/html/body/form/div[3]/footer/div[1]/div/div[4]/div[2]/div/span[1]',
        '/html/body/form/div[3]/footer/div[1]/div/div[4]/div[2]/div/span[2]'
    ]
    
    validation_messages = []
    for xpath in validation_messages_xpaths:
        elements = html_tree.xpath(xpath)
        for element in elements:
            validation_messages.append(element.text)
    
    return validation_messages


def write_to_csv(validation_messages):
    with open('scraped_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Email Validation Messages"])
        for message in validation_messages:
            writer.writerow([message])


if __name__ == "__main__":
    validation_messages = extract_validation_messages('downloaded_pages/DTU-entrepreneurship.html')
    write_to_csv(validation_messages)