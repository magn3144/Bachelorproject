import re
import csv

def extract_address_components(html_file):
    with open(html_file, 'r') as f:
        html = f.read()

    address_components = re.findall(r'<div\sclass="addr-component[^>]*>([^<]+)', html)
    address_components = [component.strip() for component in address_components]

    properties = re.findall(r'<div\sclass="text-muted">([^<]+)', html)

    rows = []
    for i in range(len(properties)):
        if i < len(address_components):
            address = address_components[i]
        else:
            address = ""

        rows.append([address, properties[i]])

    with open('scraped_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Address', 'Property'])
        writer.writerows(rows)

extract_address_components('downloaded_pages/homefinder.html')