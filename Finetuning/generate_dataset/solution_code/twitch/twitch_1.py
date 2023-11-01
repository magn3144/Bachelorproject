import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/twitch.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Define the XPath expressions for the post titles and likes
post_title_xpath = "//h2[@class='post-title']/a/text()"
likes_xpath = "//span[@class='post-likes']/text()"

# Extract the post titles and likes from the page
post_titles = tree.xpath(post_title_xpath)
likes = tree.xpath(likes_xpath)

# Prepare the data to be saved in CSV format
data = zip(post_titles, likes)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Post Title', 'Likes'])
    writer.writerows(data)