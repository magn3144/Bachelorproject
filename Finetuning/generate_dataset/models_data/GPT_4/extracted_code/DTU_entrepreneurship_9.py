import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def data_scraper():
    # parse html
    path = 'downloaded_pages/DTU_entrepreneurship.html'
    soup = BeautifulSoup(open(path, 'r'), 'html.parser')

    # find the "Departments and Centers" section and extract department names and links
    department_details = []
    
    divs = soup.find_all('div', {'div[1]/div/div[2]/nav/div[1]/div/div/div[3]'})

    for div in divs:
        for department in div.find_all('a'):
            department_name = department.get_text(strip=True)
            department_link = urljoin('https://www.entrepreneurship.dtu.dk', department.get('href'))
            department_details.append([department_name, department_link])

    # write data to csv
    with open('scraped_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Department Name', 'Department Link'])
        writer.writerows(department_details)

data_scraper()