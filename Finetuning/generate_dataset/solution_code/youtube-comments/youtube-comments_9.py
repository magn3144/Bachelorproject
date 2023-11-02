import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/youtube-comments.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Extract the verified channel name
verified_channel = tree.xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[2]/div/ytd-rich-item-renderer[5]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/div/tp-yt-paper-tooltip/div/text()')[0]

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Verified Channel'])
    writer.writerow([verified_channel])