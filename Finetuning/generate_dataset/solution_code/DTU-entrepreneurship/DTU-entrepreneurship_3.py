import csv
import requests
from lxml import html

def scrape_page(path):
    with open(path, 'r') as file:
        page_content = file.read()
    tree = html.fromstring(page_content)
    projects = tree.xpath('//label[text() = "Projects"]')
    
    project_data = []
    for project in projects:
        project_info = {}
        
        project_info['text'] = project.text_content()
        project_info['xpath'] = tree.getpath(project)
        
        project_data.append(project_info)

    return project_data

def export_to_csv(data):
    keys = data[0].keys()
    with open('scraped_data.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def main():
    local_file_path = 'downloaded_pages/DTU-entrepreneurship.html'
    project_data = scrape_page(local_file_path)
    export_to_csv(project_data)
    
main()