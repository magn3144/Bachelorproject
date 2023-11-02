import csv
from lxml import etree
            
def extract_stats_labels():
    # Define XPaths for player stats and labels
    stats_xpath = "/html/body/div[1]/div/div/div/main/div[3]/div/div[1]/div[1]/div/section[1]/div/section[4]/div[1]/div/div[3]/div/div/div[3]/a/div[2]/div[2]/div/div/span"
    labels_xpath = "/html/body/div[1]/div/div/div/main/div[3]/div/div[1]/div[1]/div/section[1]/div/section[4]/div[1]/div/div[3]/div/div/div[3]/a/div[2]/div[2]/div/div/span[1]"

    # Parse the HTML file
    tree = etree.parse('downloaded_pages/espn.html', etree.HTMLParser())
    
    # Extract player stats
    stats_elements = tree.xpath(stats_xpath)
    stats = [elem.text for elem in stats_elements]
    
    # Extract labels
    labels_elements = tree.xpath(labels_xpath)
    labels = [elem.text for elem in labels_elements]
    
    # Save data as CSV
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Stats', 'Labels'])  # Write header
        writer.writerows(zip(stats, labels))
    
extract_stats_labels()