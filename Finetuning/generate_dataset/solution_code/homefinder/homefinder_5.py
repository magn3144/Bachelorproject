import re
import csv

html_file = "downloaded_pages/homefinder.html"
target_elements = [
    '<label class="font-weight-bold">Cities Near New York, NY</label>',
    '<a class="search-internal-link d-block">'
]

with open(html_file, 'r') as file:
    html_content = file.read()

city_list = []

for element in target_elements:
    match = re.search(r'({0})(.*?)</a>'.format(element), html_content)
    if match:
        city = match.group(2).strip()
        city_list.append(city)

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['City'])
    writer.writerows(zip(city_list))