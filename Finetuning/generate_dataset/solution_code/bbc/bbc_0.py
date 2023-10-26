import requests
from lxml import html
import csv

# Define the target website
website = "bbc"

# Define the local path to the HTML file
html_file_path = "downloaded_pages/bbc.html"

# Define the category
category = "News"

# Define the web-scraping tasks
scraping_tasks = [
    ("Title", "/html/body/div[8]/div/div/div[4]/div[7]/div/div/ol/li[4]/span/div/a/span[2]"),
    ("Heading", "/html/body/div[8]/div/div/div[4]/div[12]/div/div/div[2]/div[4]/div/div[2]/ul/li/a/span"),
    ("Most Read", "/html/body/div[8]/div/div/div[5]/div/div/div[1]/div/div/h2"),
    ("Page Title", "/html/body/div[8]/div/div/div[1]/h1"),
    ("BBC News App Link", "/html/body/div[8]/div/div/div[4]/div[17]/div/div/div[2]/div/div[2]/a"),
    ("Privacy Policy Link", "/html/body/div[9]/footer/div/div/div/ul/li[3]/a"),
    ("Featured News", "/html/body/div[8]/div/div/div[4]/div[12]/div/div/div[2]/div[6]/div/div[2]/div/a/h3"),
    ("Mobile App Heading", "/html/body/div[8]/div/div/div[4]/div[17]/div/div/div[2]/div/div[2]/h3"),
    ("Summary", "/html/body/div[8]/div/div/div[4]/div[2]/div/div/div[2]/div/div[13]/div[5]/div/div[2]/div/p"),
    ("Related Content", "/html/body/div[8]/div/div/div[4]/div[2]/div/div/div[1]/div/div/div[1]/div[3]/div/h4"),
    ("Nations Slice Container", "/html/body/div[8]/div/div/div[4]/div[14]"),
    ("News Headline", "/html/body/div[8]/div/div/div[4]/div[11]/div/div/div[2]/ol/li[8]/span/div/a/span"),
    ("Status Date", "/html/body/div[8]/div/div/div[4]/div[2]/div/div/div[2]/div/div[15]/div[1]/div/div[2]/ul/li[1]/span/time/span[1]"),
    ("Sport Heading", "/html/body/div[8]/div/div/div[4]/div[16]/div/div/div[1]/div/div/a/h2"),
    ("BBC News Daily Link", "/html/body/div[8]/div/div/div[4]/div[17]/div/div/div[2]/div/div[1]/a"),
    ("Privacy Policy Link", "/html/body/div[9]/footer/div/div/div/ul/li[4]/a"),
    ("Weird Aliens", "/html/body/div[8]/div/div/div[4]/div[12]/div/div/div[2]/div[1]/div/div[2]/div/a/h3"),
    ("Get in Touch Heading", "/html/body/div[8]/div/div/div[4]/div[17]/div/div/div[2]/div/div[3]/h3"),
    ("News Summary", "/html/body/div[8]/div/div/div[4]/div[2]/div/div/div[2]/div/div[15]/div[4]/div/div[2]/div/p"),
    ("Boats Collision", "/html/body/div[8]/div/div/div[4]/div[7]/div/div/ol/li[3]/span/div/a/span[2]"),
    ("UK Home", "/html/body/div[8]/div/div/div[4]/div[18]/div/nav/ul/li[7]/ul/li[1]/a/span"),
    ("Most Watched", "/html/body/div[8]/div/div/div[4]/div[7]/div/div/div/div/div/h2"),
    ("Trust BBC News Link", "/html/body/div[8]/div/div/div[4]/div[17]/div/div/div[2]/div/div[3]/ul/li[3]/p/a"),
    ("Advertisement Link", "/html/body/div[8]/div/div/div[4]/div[2]/div/div/div[2]/div/div[4]/div/div[2]/div[1]/a"),
    ("Belgians Race Boats", "/html/body/div[8]/div/div/div[4]/div[6]/div/div/div[2]/div[3]/div/div[2]/div/a/h3"),
    ("News Daily Newsletter Heading", "/html/body/div[8]/div/div/div[4]/div[17]/div/div/div[2]/div/div[1]/h3"),
    ("Drug Use Modification", "/html/body/div[8]/div/div/div[4]/div[2]/div/div/div[2]/div/div[5]/div/div[2]/div/p"),
    ("Minimum Tax Rate", "/html/body/div[8]/div/div/div[4]/div[11]/div/div/div[2]/ol/li[4]/span/div/a/span"),
    ("Northern Ireland", "/html/body/div[8]/div/div/div[4]/div[18]/div/nav/ul/li[7]/ul/li[3]/a/span"),
    ("News Navigation Heading", "/html/body/div[8]/header/div[1]/div/div/h2"),
    ("External Link", "/html/body/div[9]/footer/div/div/div/small/span/a"),
    ("Have Your Say Link", "/html/body/div[8]/div/div/div[4]/div[17]/div/div/div[2]/div/div[3]/ul/li[1]/p/a"),
    ("Sir Patrick Stewart Visit", "/html/body/div[8]/div/div/div[4]/div[6]/div/div/div[2]/div[7]/div/div[2]/div/a/h3"),
    ("BBC World News TV", "/html/body/div[8]/div/div/div[4]/div[6]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/a/h3"),
    ("News Summary", "/html/body/div[8]/div/div/div[4]/div[2]/div/div/div[2]/div/div[13]/div[1]/div/div[2]/div/p"),
    ("West Bank Air Strike", "/html/body/div[8]/div/div/div[4]/div[11]/div/div/div[2]/ol/li[4]/span/div/a/span")
]

# Create a list to store the scraped data
scraped_data = []

# Load the HTML file
with open(html_file_path, 'r') as f:
    html_content = f.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Scrape the data for each task
for task in scraping_tasks:
    task_label, task_xpath = task
    element = tree.xpath(task_xpath)
    if element:
        scraped_data.append((task_label, element[0].text))

# Save the scraped data as a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(scraped_data)