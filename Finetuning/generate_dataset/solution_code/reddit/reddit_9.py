from lxml import html
import csv

# Define the target HTML file path
html_file_path = 'downloaded_pages/reddit.html'

# Define the XPaths for the required HTML elements
title_xpath = '/html/head/title'
community_xpath = '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[1]/div/div/div/div[3]/div[1]/div/h1'
about_community_xpath = '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/div[1]/h2'
moderators_xpath = '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[5]/div/div[1]/div/h2'

# Scrape the required information from the HTML file
tree = html.parse(html_file_path)
title = tree.xpath(title_xpath)[0].text_content().strip()
community_info = tree.xpath(community_xpath)[0].text_content().strip()
about_community = tree.xpath(about_community_xpath)[0].text_content().strip()
moderators = tree.xpath(moderators_xpath)[0].text_content().strip()

# Create the CSV file and write the scraped data
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Community Info', 'About Community', 'Moderators'])
    writer.writerow([title, community_info, about_community, moderators])