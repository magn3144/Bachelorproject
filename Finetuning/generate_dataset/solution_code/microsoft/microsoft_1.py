import csv
from lxml import etree

# Load the HTML document
with open('downloaded_pages/microsoft.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Define the XPaths of the forum topics and their corresponding links
forum_topic_xpath = "//h3[contains(@class, 'HubPageTrendingTopicsCategoryHeading')]"
forum_link_xpath = "//a[contains(@class, 'ocpArticleLink')]"

# Extract the forum topics and links
forum_topics = html_tree.xpath(forum_topic_xpath)
forum_links = html_tree.xpath(forum_link_xpath)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Forum Topic', 'Link'])  # Write header row
    for topic, link in zip(forum_topics, forum_links):
        writer.writerow([topic.text.strip(), link.get('href')])