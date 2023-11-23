import csv
from lxml import html

# open the local file
with open('downloaded_pages/imdb.html', 'r', encoding='utf-8') as file:
    page_html = file.read()

# create the HTML Element object
page_element = html.fromstring(page_html)

# define the XPaths to select data
ratings = []
for i in range(1, 251):
    xpath_rating = f'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/span/div/span/text()'
    ratings.append(page_element.xpath(xpath_rating))

# write the data into a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(ratings)