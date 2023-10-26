import csv
from lxml import html

def scrape_web_page():
    page_path = 'downloaded_pages/bleacherreport.html'
    with open(page_path, 'r') as f:
        page_content = f.read()
    
    tree = html.fromstring(page_content)
    
    h3_elements = tree.xpath('//h3')
    h3_texts = [h3.text for h3 in h3_elements]
    
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Heading'])
        writer.writerows([[h3_text] for h3_text in h3_texts])

scrape_web_page()