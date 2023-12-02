import csv
import re
from lxml import html

def get_course_info(root):
    course_info = []
    course_blocks = root.xpath('//div[contains(@class, "o-list-course__wrapper__info")]')
    for block in course_blocks:
        info = {}
        title = block.xpath(".//h2/span/text()")
        if title:
            info['Course'] = title[0]
            tp = block.xpath(".//div[@class='o-list-course__wrapper--meta']/text()")
            if tp:
                info['Type'] = tp[0]
            sem = block.xpath(".//div[@class='o-list-course__wrapper--meta']/following-sibling::text()")
            if sem:
                info['Semester'] = sem[0].strip()
        course_info.append(info)
    return course_info

def save_to_csv(data):
    keys = data[0].keys()
    with open('scraped_data.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def main():
    with open('downloaded_pages/DTU_entrepreneurship.html', 'r', encoding="utf8") as f:
        content = f.read()
    root = html.fromstring(content)
    data = get_course_info(root)
    save_to_csv(data)

if __name__ == "__main__":
    main()