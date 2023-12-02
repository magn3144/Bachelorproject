import csv
import bs4
import lxml.html as html

file_path = 'downloaded_pages/airbnb.html'
output_file = 'scraped_data.csv'

def get_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def parse_html(content):
    page = bs4.BeautifulSoup(content, 'lxml')
    return page

def extract_data(html_content):
    data = []
    listings = html_content.find_all('div', {'class': 't1jojoys dir dir-ltr'})
    for listing in listings:
        location = listing.text
        if html_content.find('div', {'class': 't1qa5xaj dir dir-ltr'}):
            stars = '5'
        else:
            stars = '0'
        data.append([location, stars])
    return data

def save_to_csv(data, output_file):
    header = ['Location', 'Stars']
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

content = get_content(file_path)
parsed_html = parse_html(content)
data = extract_data(parsed_html)
save_to_csv(data, output_file)