import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/washingtonpost.html'
target_elements = ['<figcaption class="gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs">Sierra Schuetz and Fred Flipse organize food at Co</figcaption>',
                   '<figcaption class="gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs">(Reuters)</figcaption>',
                   '<figcaption class="gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs">(Martina Tuaty/For The Washington Post)</figcaption>',
                   '<figcaption class="gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs">(iStock /iStock)</figcaption>',
                   '<figcaption class="gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs">(Recorded Books; Macmillan Audio; Bloomsbury)</figcaption>',
                   '<figcaption class="gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs">(Chris Seward/AP)</figcaption>',
                   '<figcaption class="gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs">(Celia Jacobs for The Washington Post)</figcaption>',
                   '<figcaption class="gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs">(Jasu Hu/Jasu Hu for The Washington Post)</figcaption>',
                   '<figcaption class="gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs">Former U.N. Ambassador Nikki Haley and Florida Gov</figcaption>',
                   '<figcaption class="gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs">(Kristen Zeis for The Post)</figcaption>',
                   '<figcaption class="gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs">(Nathaniel Brown for The Post)</figcaption>']

def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    figcaptions = soup.find_all('figcaption', class_='gray-dark font-xxxxs left pb-xs font--meta-text lh-sm mt-xxs')
    return [figcaption.get_text(strip=True) for figcaption in figcaptions]

scraped_data = extract_text_from_html(html_file)

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([data] for data in scraped_data)