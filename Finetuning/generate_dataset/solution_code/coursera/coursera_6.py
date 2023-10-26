import csv
from lxml import etree

def scrape_undergraduate_programs(html_file):
    tree = etree.parse(html_file)
    programs = tree.xpath("//div[contains(@class, 'megaMenuGoalItem-name')]")
    
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Program Name'])
        for program in programs:
            program_name = program.text.strip()
            writer.writerow([program_name])

scrape_undergraduate_programs('downloaded_pages/coursera.html')