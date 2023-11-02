import csv
from lxml import etree

def extract_suggested_video_title():
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Suggested Video Title'])

        # Read the local HTML file
        with open('downloaded_pages/youtube-comments.html', 'r', encoding='utf-8') as html_file:
            html = html_file.read()

        # Create an lxml HTML parser and parse the HTML content
        parser = etree.HTMLParser()
        tree = etree.fromstring(html, parser)

        # Extract the title of the suggested video
        xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[4]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[1]/div[1]/div/div[1]/a/h3/span'
        suggested_video_title = tree.xpath(xpath)[0].text.strip()

        # Write the extracted title to the CSV file
        writer.writerow([suggested_video_title])

extract_suggested_video_title()