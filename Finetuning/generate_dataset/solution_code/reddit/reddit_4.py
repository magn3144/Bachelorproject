import csv
from lxml import etree

# Function to extract text from the given HTML element using XPath
def extract_text(element):
    return element.xpath(".//text()")

# Function to extract details from social media posts screenshots
def extract_social_media_posts(tree):
    screenshots = tree.xpath("//div[contains(@class, 'tbIApBd2DM_drfZQJjIum')]")
    posts = []
    for screenshot in screenshots:
        post = extract_text(screenshot)
        posts.append(post)
    return posts

# Main scraping function
def scrape_webpage(html_path):
    # Open the HTML file and parse it as an HTML tree
    with open(html_path, "r") as file:
        html = file.read()
    tree = etree.HTML(html)
    
    # Extract social media post details
    social_media_posts = extract_social_media_posts(tree)
    
    # Write the scraped data to a CSV file
    with open("scraped_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Social Media Posts"])
        for post in social_media_posts:
            writer.writerow([post])

# Run the scraping function with the given HTML file path
scrape_webpage("downloaded_pages/reddit.html")