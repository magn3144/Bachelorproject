import csv
from bs4 import BeautifulSoup

def write_to_csv(data):
    with open('scraped_data.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        for row in data:
            writer.writerow(row)

def scrape_file(file_path):
    with open(file_path, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    results = []

    elements = soup.find_all('div', class_='t1jojoys dir dir-ltr')

    for element in elements:
        location = element.text.split(',')[0]
        try:
            distance = element.text.split(',')[1]
        except IndexError:
            distance = "N/A"
        results.append([location, distance])

    return results

if __name__ == "__main__":
    scrape_results = scrape_file("downloaded_pages/airbnb.html")
    write_to_csv(scrape_results)