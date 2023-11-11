import csv
from lxml import etree

# Define the local path to the HTML file
html_file_path = "downloaded_pages/urbandictionary.html"

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file_path, parser)

# Define the HTML elements and their corresponding XPaths
elements = [
    {"element": "a", "class": "whitespace-nowrap text-light-charcoal hover:text-black dark:hover:text-white", "xpath": "/html/body/div/div/main/div/div[4]/aside/div[2]/div[2]/ul/li[9]/a"},
    {"element": "a", "class": "block text-white font-bold px-3 hover:text-chartreuse-yellow", "xpath": "/html/body/div/header/div[2]/div[1]/div/div/ul/li[5]/a"},
    {"element": "span", "class": "bg-black p-1 text-screamin-green", "xpath": "/html/body/div/div/main/div/div[4]/section/div[4]/a/span"},
    {"element": "span", "class": "text-xs font-bold uppercase ml-1", "xpath": "/html/body/div/div/main/div/div[4]/section/div[3]/div/div[5]/a/span"},
    {"element": "div", "class": "mb-1", "xpath": "/html/body/div/div/main/div/div[4]/aside/div[2]/div[2]/div"},
    {"element": "a", "class": "text-denim dark:text-fluorescent hover:text-limon-lime", "xpath": "/html/body/div/div/main/div/div[4]/section/div[1]/div/div[4]/a"},
    {"element": "a", "class": "nav-link", "xpath": "/html/body/div/header/div[2]/div[1]/div/div/ul/li[1]/div/div/ul/li[8]/a"},
    {"element": "span", "class": "ml-2", "xpath": "/html/body/div/div/main/div/div[4]/aside/div[1]/div/a/span"},
    {"element": "a", "class": "text-denim dark:text-fluorescent hover:text-limon-lime", "xpath": "/html/body/div/div/main/div/div[4]/section/div[3]/div/div[4]/a"},
    {"element": "a", "class": "block text-white font-bold px-3 hover:text-chartreuse-yellow", "xpath": "/html/body/div/header/div[2]/div[1]/div/div/ul/li[4]/a"},
    {"element": "span", "class": "text-sm ml-2", "xpath": "/html/body/div/div/main/div/div[4]/aside/div[1]/ul/li[2]/a/span"},
    {"element": "a", "class": "autolink", "xpath": "/html/body/div/div/main/div/div[4]/section/div[9]/div/div[2]/a[1]"},
    {"element": "a", "class": "nav-link", "xpath": "/html/body/div/header/div[2]/div[1]/div/div/ul/li[1]/div/div/ul/li[22]/a"},
    {"element": "span", "class": "text-xs font-bold ml-2", "xpath": "/html/body/div/div/main/div/div[4]/section/div[4]/div/div[5]/div/button[2]/span"},
    {"element": "a", "class": "autolink", "xpath": "/html/body/div/div/main/div/div[4]/section/div[9]/div/div[2]/a[2]"},
    {"element": "a", "class": "autolink", "xpath": "/html/body/div/div/main/div/div[4]/section/div[6]/div/div[3]/a[2]"},
    {"element": "span", "class": "text-xs font-bold ml-2", "xpath": "/html/body/div/div/main/div/div[4]/section/div[6]/div/div[5]/div/button[2]/span"},
    {"element": "a", "class": "whitespace-nowrap text-light-charcoal hover:text-black dark:hover:text-white", "xpath": "/html/body/div/div/main/div/div[4]/aside/div[2]/div[2]/ul/li[8]/a"},
    {"element": "a", "class": "whitespace-nowrap text-light-charcoal hover:text-black dark:hover:text-white", "xpath": "/html/body/div/div/main/div/div[4]/aside/div[2]/div[2]/ul/li[1]/a"},
    {"element": "span", "class": "text-xs font-bold ml-2", "xpath": "/html/body/div/div/main/div/div[4]/section/div[7]/div/div[5]/div/button[1]/span"},
    {"element": "a", "class": "text-denim dark:text-fluorescent hover:text-limon-lime", "xpath": "/html/body/div/div/main/div/div[4]/section/div[9]/div/div[4]/a"},
    {"element": "a", "class": "nav-link", "xpath": "/html/body/div/header/div[2]/div[1]/div/div/ul/li[1]/div/div/ul/li[21]/a"},
    {"element": "span", "class": "text-xs font-bold ml-2", "xpath": "/html/body/div/div/main/div/div[4]/section/div[6]/div/div[5]/div/button[1]/span"},
    {"element": "a", "class": "autolink", "xpath": "/html/body/div/div/main/div/div[4]/section/div[6]/div/div[2]/a[2]"},
    {"element": "a", "class": "nav-link", "xpath": "/html/body/div/header/div[1]/div[2]/div/div/ul/li[2]/ul/li[27]/a"},
    {"element": "span", "class": "text-xs font-bold ml-2", "xpath": "/html/body/div/div/main/div/div[4]/section/div[9]/div/div[5]/div/button[1]/span"},
    {"element": "a", "class": "autolink", "xpath": "/html/body/div/div/main/div/div[4]/section/div[9]/div/div[2]/a[3]"},
    {"element": "a", "class": "autolink", "xpath": "/html/body/div/div/main/div/div[4]/section/div[10]/div/div[3]/a[3]"},
    {"element": "span", "class": "bg-black p-1 text-white", "xpath": "/html/body/div/div/main/div/div[4]/section/div[7]/a/span"},
    {"element": "a", "class": "text-denim dark:text-fluorescent hover:text-limon-lime", "xpath": "/html/body/div/div/main/div/div[4]/section/div[10]/div/div[4]/a"},
    {"element": "a", "class": "autolink", "xpath": "/html/body/div/div/main/div/div[4]/section/div[1]/div/div[2]/a[3]"},
    {"element": "span", "class": "bg-black p-1 text-screamin-green", "xpath": "/html/body/div/div/main/div/div[4]/section/div[9]/a/span"},
    {"element": "a", "class": "autolink", "xpath": "/html/body/div/div/main/div/div[4]/section/div[3]/div/div[2]/a[3]"},
    {"element": "a", "class": "nav-link", "xpath": "/html/body/div/header/div[2]/div[1]/div/div/ul/li[1]/div/div/ul/li[23]/a"},
    {"element": "span", "class": "text-xs font-bold ml-2", "xpath": "/html/body/div/div/main/div/div[4]/section/div[7]/div/div[5]/div/button[2]/span"},
    {"element": "a", "class": "autolink", "xpath": "/html/body/div/div/main/div/div[4]/section/div[4]/div/div[3]/a[3]"},
    {"element": "a", "class": "nav-link", "xpath": "/html/body/div/header/div[2]/div[1]/div/div/ul/li[1]/div/div/ul/li[4]/a"},
    {"element": "span", "class": "text-xs font-bold ml-2", "xpath": "/html/body/div/div/main/div/div[4]/section/div[1]/div/div[5]/div