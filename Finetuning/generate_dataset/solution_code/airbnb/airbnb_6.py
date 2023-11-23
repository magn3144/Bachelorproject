from bs4 import BeautifulSoup
import csv
import os

def extract_data(file):
    with open(file, 'r', encoding='utf-8') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
    
    # Get the <ul> parent element
    ul = soup.find('ul', {'class': 'gjo09wt dir dir-ltr'})

    # Get the <li> child elements with class "dir dir-ltr"
    li_elems = ul.find_all('li', {'class': 'dir dir-ltr'})

    # Get the link from the <a> child elements
    links_elems = [li.find('a') for li in li_elems]
    links = [link['href'] if link else None for link in links_elems]

    # Get the text from the first <span> child element
    spans_elems = [li.find('span') for li in li_elems]
    spans = [span.text if span else None for span in spans_elems]

    # Save the two lists as seperate columns in a CSV file
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Location", "Link"])
        for span, link in zip(spans, links):
            writer.writerow([span, link])

file_path = os.path.join('downloaded_pages', 'airbnb.html')
extract_data(file_path)