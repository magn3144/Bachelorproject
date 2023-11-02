import csv
from lxml import etree

def extract_comments():
    # Load the HTML file
    tree = etree.parse('downloaded_pages/youtube-comments.html')

    # Find all comment elements
    comment_elements = tree.xpath('//span[@class="style-scope ytd-comment-renderer style-scope ytd-comment-renderer"]')

    # Extract the text content of comments
    comments = [elem.text.strip() for elem in comment_elements]

    # Save comments as CSV
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Comment'])
        writer.writerows([[comment] for comment in comments])

# Run the function to extract comments
extract_comments()