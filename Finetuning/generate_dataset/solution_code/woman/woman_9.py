import csv
from lxml import etree

def extract_links():
    # Read the HTML file
    with open('downloaded_pages/woman.html', 'r') as file:
        html = file.read()
    
    # Parse the HTML
    tree = etree.HTML(html)
    
    # Find all anchor elements that contain 'Klummer fra læserne' text
    links = tree.xpath("//a[contains(text(), 'Klummer fra læserne')]/@href")
    
    # Remove duplicates
    links = list(set(links))
    
    # Save links as CSV
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['URL'])
        writer.writerows([[link] for link in links])

# Call the function
extract_links()