import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/microsoft.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Initialize the scraped data list
scraped_data = []

# Web-scraping task: Get the text from the given HTML elements
text_1 = tree.xpath('/html/body/div/div[2]/div/div/header/div/div/nav/ul/li[6]/div/ul/li[2]/a/text()')[0]
text_2 = tree.xpath('/html/body/div/div[4]/div/div/div/footer/nav/div[1]/div[1]/ul/li[1]/a/text()')[0]
text_3 = tree.xpath('/html/body/div/div[4]/div/div/div/footer/div/a[2]/span/text()')[0]
text_4 = tree.xpath('/html/body/div/div[2]/div/div/header/div/div/div[4]/div[1]/nav/ul/li/div/ul/li[3]/span/text()')[0]
text_5 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[3]/div/section/h2/text()')[0]
text_6 = tree.xpath('/html/body/div/div[2]/div/div/header/div/div/div[4]/div[1]/nav/ul/li/div/ul/li[1]/h2/text()')[0]
text_7 = tree.xpath('/html/body/div/section/div/div/div/div/article/header/nav/div/div/div[1]/ul/li[2]/a/div/div[2]/text()')[0]
text_8 = tree.xpath('/html/body/div/div[4]/div/div/div/footer/nav/div[1]/div[3]/div/text()')[0]
text_9 = tree.xpath('/html/body/div/section/div/div/div/div/article/header/div/h1/text()')[0]
text_10 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[3]/div/section/div/div[1]/div[2]/h3/text()')[0]
text_11 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[1]/div/section/div/div/div[4]/h3/text()')[0]
text_12 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[3]/div/section/div/div[2]/div[4]/p[1]/text()')[0]
text_13 = tree.xpath('/html/body/div/div[4]/div/div/div/footer/div/a[2]/svg/title/text()')[0]
text_14 = tree.xpath('/html/body/div/div[4]/div/div/div/footer/div/nav/ul/li[8]/text()')[0]
text_15 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[1]/div/section/div/div/div[3]/ul/li[3]/p/a/text()')[0]
text_16 = tree.xpath('/html/body/div/div[2]/div/div/header/div/div/div[4]/div[1]/nav/ul/li/div/ul/li[1]/ul/li[4]/a/text()')[0]
text_17 = tree.xpath('/html/body/div/div[4]/div/div/div/footer/div/noscript/a/span/text()')[0]
text_18 = tree.xpath('/html/body/div/div[2]/div/div/header/div/div/div[2]/a/span/text()')[0]
text_19 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[6]/div/section/div/div/div[2]/h2/text()')[0]
text_20 = tree.xpath('/html/body/div/div[3]/div[2]/div[4]/div[2]/text()')[0]
text_21 = tree.xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/text()')[0]
text_22 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[3]/div/section/div/div[2]/div[4]/h3/text()')[0]
text_23 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[1]/div/section/div/div/div[3]/h3/text()')[0]
text_24 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[5]/div/section/div/div/div[1]/p[1]/text()')[0]
text_25 = tree.xpath('/html/body/div/div[4]/div/div/div/footer/div/noscript/a/svg/title/text()')[0]
text_26 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[1]/div/section/div/div/div[2]/ul/li[3]/p/a/text()')[0]
text_27 = tree.xpath('/html/body/div/div[4]/div/div/div/footer/div/nav/ul/li[3]/a/text()')[0]
text_28 = tree.xpath('/html/body/div/div[2]/div/div/header/div/div/div[4]/form/button/span[1]/text()')[0]
text_29 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[4]/div/section/h2/text()')[0]
text_30 = tree.xpath('/html/body/div/section/div/div/div/div/article/header/nav/div/div/div[1]/ul/li[1]/a/div/div[2]/text()')[0]
text_31 = tree.xpath('/html/body/div/div[2]/div/div/header/div/div/div[4]/div[2]/div/div/text()')[0]
text_32 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[4]/div/section/div/div/div[3]/h3/text()')[0]
text_33 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[4]/div/section/div/div/div[4]/h3/text()')[0]
text_34 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[3]/div/section/div/div[2]/div[2]/p[1]/text()')[0]
text_35 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[3]/div/section/div/div[2]/div[4]/p[2]/a/text()')[0]
text_36 = tree.xpath('/html/body/div/div[4]/div/div/div/footer/nav/div[1]/div[3]/ul/li[2]/a/text()')[0]
text_37 = tree.xpath('/html/body/div/div[2]/div/div/header/div/div/div[4]/button/span/text()')[0]
text_38 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[1]/div/section/h2/text()')[0]
text_39 = tree.xpath('/html/body/div/section/div/div/div/div/article/header/nav/div/div/div[1]/ul/li[7]/a/div/div[2]/text()')[0]
text_40 = tree.xpath('/html/body/div/div[3]/div[2]/div[4]/div[1]/text()')[0]
text_41 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[3]/div/section/div/div[2]/div[2]/h3/text()')[0]
text_42 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[4]/div/section/div/div/div[1]/h3/text()')[0]
text_43 = tree.xpath('/html/body/div/section/div/div/div/div/article/div[2]/div/section/div/div/div[2]/p[1]/text()')[0]

# Add the scraped data to the list
scraped_data.append(text_1)
scraped_data.append(text_2)
scraped_data.append(text_3)
scraped_data.append(text_4)
scraped_data.append(text_5)
scraped_data.append(text_6)
scraped_data.append(text_7)
scraped_data.append(text_8)
scraped_data.append(text_9)
scraped_data.append(text_10)
scraped_data.append(text_11)
scraped_data.append(text_12)
scraped_data.append(text_13)
scraped_data.append(text_14)
scraped_data.append(text_15)
scraped_data.append(text_16)
scraped_data.append(text_17)
scraped_data.append(text_18)
scraped_data.append(text_19)
scraped_data.append(text_20)
scraped_data.append(text_21)
scraped_data.append(text_22)
scraped_data.append(text_23)
scraped_data.append(text_24)
scraped_data.append(text_