import csv
from lxml import html

# Load HTML file
tree = html.parse("downloaded_pages/arxiv.html")

# Create CSV file for storing scraped data
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Find all entries
    entries = tree.xpath('//div[@class="entry"]')

    # Iterate over entries
    for entry in entries:
        subjects = entry.xpath('.//span[@class="descriptor"][text()="Subjects:"]/following-sibling::span')
        subject_list = [subject.text_content() for subject in subjects]

        # Write subject data to CSV file
        writer.writerow(subject_list)