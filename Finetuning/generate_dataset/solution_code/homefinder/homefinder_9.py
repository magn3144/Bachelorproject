import csv
from lxml import html

def scrape_mortgage_info(input_file):
    tree = html.parse(input_file)

    mortgage_element = tree.xpath("/html/body/div/div/div/section/div[1]/div[4]/div[2]/div[4]/div[1]/div[2]/p")
    mortgage_info = mortgage_element[0].text.strip()
    
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Mortgage Info'])
        writer.writerow([mortgage_info])

scrape_mortgage_info('downloaded_pages/homefinder.html')