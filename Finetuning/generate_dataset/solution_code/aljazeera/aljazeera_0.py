import csv
from lxml import etree

# Define the HTML elements and their corresponding XPaths
elements = [
    {"element": "title", "xpath": "/html/head/title"},
    {"element": "title", "xpath": "/html/body/div[1]/div/div[2]/div[1]/div/header/div[3]/button/svg/title"},
    {"element": "h2", "xpath": "/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div[2]/h2"},
    {"element": "h2", "xpath": "/html/body/div[1]/div/div[2]/div[1]/div/header/nav/h2"},
    {"element": "a", "xpath": "/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div[2]/p/a"},
    {"element": "a", "xpath": "/html/body/div[1]/div/div[2]/div[1]/div/header/div[1]/a[1]"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[9]/div[2]/div[1]/h3/a/span"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[2]/div[1]/div/header/nav/ul/li[1]/div/ul/li[3]/a/span"},
    {"element": "div", "xpath": "/html/body/div[1]/div/div[3]/div/div[1]/div/h1/div"},
    {"element": "p", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[3]/div[2]/div[2]/div/p"},
    {"element": "h3", "xpath": "/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div[2]/div/h3"},
    {"element": "h3", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div/div/h3"},
    {"element": "h4", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div/div/h4"},
    {"element": "title", "xpath": "/html/body/div[1]/div/div[4]/div[1]/footer/div[2]/div[1]/ul/li[2]/a/svg/title"},
    {"element": "h2", "xpath": "/html/body/div[1]/div/div[3]/div/main/h2"},
    {"element": "a", "xpath": "/html/body/div[1]/div/div[2]/div[1]/div/header/div[1]/a[2]"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/a[1]/span"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[2]/div[1]/div/header/nav/ul/li[5]/a/span"},
    {"element": "p", "xpath": "/html/body/div[1]/div/div[3]/div/main/div/ul/li[1]/article/div[2]/div[2]/div/p"},
    {"element": "title", "xpath": "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/button[1]/svg/title"},
    {"element": "h2", "xpath": "/html/body/div[1]/div/div[2]/div[1]/div/header/div[1]/h2"},
    {"element": "a", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div/form/div[2]/a"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[3]/div/main/div/ul/li[4]/article/div[2]/div[1]/h3/a/span"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[3]/div/main/div/ul/li[4]/article/div[2]/footer/div/div/div/div/span[2]"},
    {"element": "p", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[1]/div[2]/div[2]/div/p"},
    {"element": "title", "xpath": "/html/body/div[1]/div/div[4]/div[1]/footer/div[2]/div[1]/ul/li[5]/a/svg/title"},
    {"element": "h2", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/h2"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[4]/div[1]/footer/div[1]/ul/li[3]/div/ul/li[3]/a/span"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[4]/div[1]/footer/div[1]/ul/li[3]/div/ul/li[6]/a/span"},
    {"element": "p", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[6]/div[2]/div[2]/div/p"},
    {"element": "title", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[3]/div[2]/footer/div/div[1]/svg/title"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div/form/div[1]/div[3]/span"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[10]/div[2]/footer/div/div/div/div/span[2]"},
    {"element": "p", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[5]/div[2]/div[2]/div/p"},
    {"element": "title", "xpath": "/html/body/div[1]/div/div[2]/div[1]/div/header/div[3]/div[2]/div/a/div/svg/title"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[3]/div/main/div/ul/li[1]/article/div[2]/div[1]/h3/a/span"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[2]/div[1]/div/header/nav/ul/li[1]/a/span"},
    {"element": "p", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[10]/div[2]/div[2]/div/p"},
    {"element": "title", "xpath": "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/button[2]/svg/title"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[4]/div[1]/footer/div[2]/div[3]/span"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[8]/div[2]/footer/div/div/div/div/span[1]"},
    {"element": "p", "xpath": "/html/body/div[1]/div/div[4]/div[1]/footer/div[2]/div[1]/p"},
    {"element": "title", "xpath": "/html/body/div[1]/div/div[2]/div[1]/div/header/div[4]/div[3]/button/svg/title"},
    {"element": "span", "xpath": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div/div/div/span"},
]

# Scrape the page using the given XPaths
result = []
with open('