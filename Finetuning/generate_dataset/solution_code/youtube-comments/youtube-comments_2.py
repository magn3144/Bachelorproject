import csv
from lxml import html

# Define the XPath for channel name
channel_name_xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[55]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/div/tp-yt-paper-tooltip/div'

# Load the HTML file
with open('downloaded_pages/youtube-comments.html', 'r') as file:
    html_data = file.read()

# Parse the HTML
tree = html.fromstring(html_data)

# Extract the channel name
channel_name_element = tree.xpath(channel_name_xpath)
channel_name = channel_name_element[0].text.strip()

# Write the channel name to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Channel Name'])
    writer.writerow([channel_name])