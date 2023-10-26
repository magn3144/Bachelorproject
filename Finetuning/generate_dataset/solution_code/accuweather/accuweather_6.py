import csv
from lxml import etree

# Load the HTML file
html_file = "downloaded_pages/accuweather.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# Define the XPath expressions
title_xpath = "/html/body/div/div[7]/div[2]/div/div[@class='right-rail-article']/div/a/div[@class='right-rail-article__title']"
time_xpath = "/html/body/div/div[7]/div[2]/div/div[@class='right-rail-article']/div/a/div[@class='right-rail-article__time']"

# Scrape the title and time of the right-rail article
tree = etree.HTML(html_content)
titles = tree.xpath(title_xpath)
times = tree.xpath(time_xpath)

# Prepare the data for CSV
data = []
for title, time in zip(titles, times):
    data.append([title.text.strip(), time.text.strip()])

# Save the data as a CSV file
output_file = "scraped_data.csv"
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Time"])
    writer.writerows(data)