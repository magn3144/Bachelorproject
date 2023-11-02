import csv
from lxml import etree


def get_department_names():
    with open('downloaded_pages/usajobs.html', 'r') as f:
        html = f.read()

    tree = etree.HTML(html)

    department_names = []
    department_elements = tree.xpath('//h5[@class="usajobs-search-result--core__department"]')

    for element in department_elements:
        department_name = element.text.strip()
        department_names.append(department_name)

    return department_names


def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Department Name'])
        writer.writerows(data)


if __name__ == '__main__':
    department_names = get_department_names()
    save_to_csv(department_names)