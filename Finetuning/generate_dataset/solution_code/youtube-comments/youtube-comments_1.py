from html.parser import HTMLParser
import csv

# Set the local path to the HTML file
file_path = 'downloaded_pages/youtube-comments.html'

# Set the category
category = 'Social Media'

# Set the XPath for the upload date element
upload_date_xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[20]/div/ytd-rich-item-renderer[3]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]'

# Create a parser for extracting the upload date
class UploadDateParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.upload_date = None

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'inline-metadata-item style-scope ytd-video-meta-block':
                    self.upload_date = True
                    break

    def handle_data(self, data):
        if self.upload_date:
            self.upload_date = data
            self.upload_date = self.upload_date.strip()
            self.upload_date = self.upload_date.replace(' ago', '')

# Create an instance of the upload date parser
upload_date_parser = UploadDateParser()

# Parse the HTML file
with open(file_path, 'r') as html_file:
    upload_date_parser.feed(html_file.read())

# Get the upload date
upload_date = upload_date_parser.upload_date

# Save the data as CSV
with open('scraped_data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Category', 'Upload Date'])
    csv_writer.writerow([category, upload_date])