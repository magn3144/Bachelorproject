import csv
from html.parser import HTMLParser

# Define a custom HTML parser
class BugReportHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.bug_reports = []

    def handle_data(self, data):
        data = data.strip()
        if data:
            self.bug_reports.append(data)

# Read the HTML file
with open('downloaded_pages/boardgamegeek.html', 'r') as f:
    html_content = f.read()

# Create an instance of the HTML parser
parser = BugReportHTMLParser()
# Feed the HTML content to the parser
parser.feed(html_content)

# Save the bug reports as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Bug Reports'])
    for report in parser.bug_reports:
        writer.writerow([report])