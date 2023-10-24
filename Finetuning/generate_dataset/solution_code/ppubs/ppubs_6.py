from bs4 import BeautifulSoup
import csv

html_path = 'downloaded_pages/ppubs.html'
output_csv = 'scraped_data.csv'

with open(html_path, 'r') as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, 'html.parser')

data = []

for li_element in soup.find_all('li'):
    li_text = li_element.text.strip()

    xpath_element = soup.find(text=li_text)
    xpath = xpath_element.parent.name

    data.append([li_text, xpath])

with open(output_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['List', 'XPath'])
    writer.writerows(data)