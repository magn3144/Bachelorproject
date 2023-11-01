import csv
import lxml.html

def scrape_doodle_title(html_file):
    with open(html_file, 'r') as f:
        page_content = f.read()

    root = lxml.html.fromstring(page_content)
    doodle_title_element = root.xpath("/html/body/div[2]/div/ul/li[3]/h3")[0]
    doodle_title = doodle_title_element.text.strip()

    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Category', 'Doodle Title'])
        writer.writerow(['Educational Websites', doodle_title])

scrape_doodle_title('downloaded_pages/google.html')