import csv
from lxml import html

# read the html file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# convert it into an html element tree
tree = html.fromstring(page_content)

# get movie titles
movie_titles = tree.xpath('//div[@class="lister-list"]/div//a/h3/text()')

# write the data into a CSV file
with open('scraped_data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Movie Title'])
    for title in movie_titles:
        writer.writerow([title])