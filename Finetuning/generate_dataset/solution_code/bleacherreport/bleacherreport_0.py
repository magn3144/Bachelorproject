import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/bleacherreport.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Define the list of web-scraping tasks
scraping_tasks = []

# Add the scraping tasks based on the provided HTML elements and XPaths
scraping_tasks.append({
    'element': soup.select_one('div.title').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[1]/div/ul/li[9]/div/a/div[1]/div[1]'
})
scraping_tasks.append({
    'element': soup.select_one('title').text,
    'xpath': '/html/body/div[1]/div/header/div/div[2]/div/div[1]/a/div/svg/title'
})
scraping_tasks.append({
    'element': soup.select_one('h3').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[11]/li/div[1]/h3'
})
scraping_tasks.append({
    'element': soup.select_one('h3').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[124]/li/div[3]/a[2]/h3'
})
scraping_tasks.append({
    'element': soup.select_one('a').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[178]/li/div[1]/h3/a'
})
scraping_tasks.append({
    'element': soup.select_one('a.typography -heading-4 -text--tertiary.navLink').text,
    'xpath': '/html/body/div[1]/div/header/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]/div[1]/a[1]'
})
scraping_tasks.append({
    'element': soup.select_one('span.provider').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[26]/li/span'
})
scraping_tasks.append({
    'element': soup.select_one('p').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[89]/li/div[1]/p'
})
scraping_tasks.append({
    'element': soup.select_one('p').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[6]/li/div[1]/p[2]'
})
scraping_tasks.append({
    'element': soup.select_one('div.title').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[1]/div/ul/li[5]/div/a/div[1]/div[1]'
})
scraping_tasks.append({
    'element': soup.select_one('title').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[144]/li/div[2]/a/svg/title'
})
scraping_tasks.append({
    'element': soup.select_one('h3').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[80]/li/div[1]/h3'
})
scraping_tasks.append({
    'element': soup.select_one('h3').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[35]/li/div[1]/h3'
})
scraping_tasks.append({
    'element': soup.select_one('a').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[143]/li/div[1]/h3/a'
})
scraping_tasks.append({
    'element': soup.select_one('a').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/footer/div/ul[2]/li[9]/a'
})
scraping_tasks.append({
    'element': soup.select_one('span.provider').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[183]/li/span'
})
scraping_tasks.append({
    'element': soup.select_one('p').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[114]/li/div[1]/p'
})
scraping_tasks.append({
    'element': soup.select_one('div.teamName').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[1]/div/ul/li[10]/div/a/div[3]/div[3]'
})
scraping_tasks.append({
    'element': soup.select_one('title').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[110]/li/div[2]/a/svg/title'
})
scraping_tasks.append({
    'element': soup.select_one('h3').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[153]/li/div[1]/h3'
})
scraping_tasks.append({
    'element': soup.select_one('h3').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[21]/li/div[3]/a[2]/h3'
})
scraping_tasks.append({
    'element': soup.select_one('a').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[115]/li/div[1]/h3/a'
})
scraping_tasks.append({
    'element': soup.select_one('a.typography -heading-4 -text--tertiary.navLink').text,
    'xpath': '/html/body/div[1]/div/header/div/div[2]/div/div[3]/div/div[2]/div[1]/div[4]/a'
})
scraping_tasks.append({
    'element': soup.select_one('span.provider').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[89]/li/span'
})
scraping_tasks.append({
    'element': soup.select_one('p').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[169]/li/div[1]/p'
})
scraping_tasks.append({
    'element': soup.select_one('div.teamName').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[1]/div/ul/li[13]/div/a/div[2]/div[3]'
})
scraping_tasks.append({
    'element': soup.select_one('title').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/footer/div/svg/title'
})
scraping_tasks.append({
    'element': soup.select_one('h3').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article/div/div/ol/div[26]/li/div[3]/a[2]/h3'
})
scraping_tasks.append({
    'element': soup.select_one('h3').text,
    'xpath': '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/article