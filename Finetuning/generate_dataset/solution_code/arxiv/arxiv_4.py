import csv
from lxml import html

def extract_main_heading():
    # Open HTML file
    with open("downloaded_pages/arxiv.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    
    # Parse the HTML
    tree = html.fromstring(html_content)
    
    # Find the main heading
    main_heading_element = tree.xpath("/html/body/div[4]/div/h1")[0]
    main_heading = main_heading_element.text_content().strip()
    
    # Save the scraped data as CSV
    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Main Heading"])
        writer.writerow([main_heading])

if __name__ == "__main__":
    extract_main_heading()