You are given a web page, the category of the page, randomly selected html elements on that page, the local path to the HTML file that should be scraped and a web-scraping task that you should solve.

Here are some randomly selected HTML elements (containing text), and their corresponding XPaths from the target page:
<a class="l1ovpqvx c1kblhex dir dir-ltr">Airbnb-friendly apartments</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[2]/ul/li[6]/a
----------------
<a class="_r243u8q l1ovpqvx dir dir-ltr">Terms</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[2]/section/div[1]/div[2]/div/div[2]/span[2]/ol/li[1]/a
----------------
<span class="u17llcap dir dir-ltr">Learn about Guest Favorites, the most loved homes </span>
/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/h1/div[1]/a/span
----------------
<span class="dir dir-ltr">Nov 18 – 25</span>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[10]/div/div[2]/div/div/div/div/div/div[2]/div[3]/span/span
----------------
<div class="db9tcim dir dir-ltr" id="category-bar-description">17 of 61 Airbnb Categories showing</div>
/html/body/div[5]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[1]
----------------
<div class="t1qa5xaj dir dir-ltr">Guest favorite</div>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[20]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div
----------------
<h2 class="hifxi0b dir dir-ltr">Inspiration for future getaways</h2>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[1]/div/div/div/div/h2
----------------
<h2 id="footerHeading">Site Footer</h2>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/span/h2
----------------
<h3 class="trsc28b dir dir-ltr">Airbnb</h3>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/h3
----------------
<a class="l1ovpqvx c1kblhex dir dir-ltr">Airbnb.org emergency stays</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/ul/li[6]/a
----------------
<a class="l1ovpqvx c1kblhex dir dir-ltr">Careers</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/ul/li[3]/a
----------------
<span class="u17llcap dir dir-ltr">Learn about Guest Favorites, the most loved homes </span>
/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/h1/div[3]/a/span
----------------
<span class="t4m7o8q t1mat252 dir dir-ltr">Glasgow</span>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[1]/div/div/div/div/div/div[2]/div[1]/ul/li[60]/a/span[1]
----------------
<div class="t1jojoys dir dir-ltr" id="title_689161363553525770">Nykøbing Sjælland, Denmark</div>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[35]/div/div[2]/div/div/div/div/div/div[2]/div[1]
----------------
<div class="t1jojoys dir dir-ltr" id="title_43448743">Frederiksværk, Denmark</div>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[13]/div/div[2]/div/div/div/div/div/div[2]/div[1]
----------------
<h3 class="trsc28b dir dir-ltr">Support</h3>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[1]/h3
----------------
<a class="l1ovpqvx c1kblhex dir dir-ltr">Report neighborhood concern</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[1]/ul/li[6]/a
----------------
<a class="l1ovpqvx c1kblhex dir dir-ltr">New features</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/ul/li[2]/a
----------------
<span class="u17llcap dir dir-ltr">Learn about Guest Favorites, the most loved homes </span>
/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/h1/div[2]/div/a/span
----------------
<span class="t4m7o8q t1mat252 dir dir-ltr">Santorini</span>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[1]/div/div/div/div/div/div[2]/div[1]/ul/li[38]/a/span[1]
----------------
<div class="t1qa5xaj dir dir-ltr">Guest favorite</div>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[13]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div
----------------
<h3 class="trsc28b dir dir-ltr">Hosting</h3>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[2]/h3
----------------
<a class="l1ovpqvx c1kblhex dir dir-ltr">Community forum</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[2]/ul/li[4]/a
----------------
<span class="a8jt5op dir dir-ltr">395 kr DKK per night</span>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[29]/div/div[2]/div/div/div/div/div/div[2]/div[4]/div/div/span/span
----------------
<div class="t1qa5xaj dir dir-ltr">Guest favorite</div>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[12]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div
----------------
<a class="_r243u8q l1ovpqvx dir dir-ltr">Privacy</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[2]/section/div[3]/div[1]/div/div[2]/span[2]/ol/li[3]/a
----------------
<span class="a8jt5op dir dir-ltr">979 kr DKK per night</span>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[23]/div/div[2]/div/div/div/div/div/div[2]/div[4]/div/div/span/span
----------------
<div class="t1qa5xaj dir dir-ltr">Guest favorite</div>
Do NOT include these directly in your code!

The page is from this website: airbnb

The local path to the HTML file is downloaded_pages/airbnb.html

The category is: Tourism

The task is: Get the text and link of each location under the "popular" tab under the "Inspiration for future getaways" header.

Now generate a python script that solves this task.
Make sure the script works when I run it, without any modifications.
The script you generate should always save the scraped data as a CSV file with the name 'scraped_data.csv'.
You can use the given HTML elements above to gain information about the page. ### Response: ```

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_html_text(url):
    r = requests.get(url)
    return r.text

def get_text_and_link(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    locations = soup.find_all('div', class_='_11zzoax8')
    text_and_link = []
    for location in locations:
        text = location.find('span', class_='_1q32f80g').text
        link = location.find('a', class_='_1q32f80g')['href']
        text_and_link.append((text, link))
    return text_and_link

def get_text_and_link_from_url(url):
    html_text = get_html_text(url)
    return get_text_and_link(html_text)

def get_text_and_link_from_file(file_path):
    with open(file_path, 'r') as f:
        html_text = f.read()
    return get_text_and_link(html_text)

def get_text_and_link_from_urls(urls):
    text_and_link = []
    for url in urls:
        text_and_link.extend(get_text_and_link_from_url(url))
    return text_and_link

def get_text_and_link_from_files(file_paths):
    text_and_link = []
    for file_path in file_paths:
        text_and_link.extend(get_text_and_link_from_file(file_path))
    return text_and_link

def get_text_and_link_from_url_and_file(url, file_path):
    text_and_link = get_text_and_link_from_url(url)
    text_and_link.extend(get_text_and_link_from_file(file_path))
    return text_and_link

def get_text_and_link_from_url_and_files(url, file_paths):
    text_and_link = get_text_and_link_from_url(url)
    text_and_link.extend(get_text_and_link_from_files(file_paths))
    return text_and_link

def get_text_and_link_from_file_and_file(file_path_1, file_path_2):
    text_and_link = get_text_and_link_from_file(file_path_1)
    text_and_link.extend(get_text_and_link_from_file(file_path_2))
    return text_and_link

def get_text_and_link_from_file_and_files(file_path_1, file_paths):
    text_and_link = get_text_and_link_from_file(file_path_1)
    text_and_link.extend(get_text_and_link_from_files(file_paths))
    return text_and_link

def get_text_and_link_from_urls_and_files(urls, file_paths):
    text_and_link = get_text_and_link_from_urls(urls)
    text_and_link.extend(get_text_and_link_from_files(file_paths))
    return text_and_link

def get_text_and_link_from_url_and_urls_and_files(url, urls, file_paths):
    text_and_link = get_text_and_link_from_url(url)
    text_and_link.extend(get_text_and_link_from_urls(urls))
    text_and_link.extend(get_text_and_link_from_files(file_paths))
    return text_and_link

def get_text_and_link_from_url_and_urls_and_files_and_files(url, urls, file_paths_1, file_paths_2):
    text_and_link = get_text_and_link_from_url(url)
    text_and_link.extend(get_text_and_link_from_urls(urls))
    text_and_link.extend(get_text_and_link_from_files(file_paths_1))
    text_and_link.extend(get_text_and_link_from_files(file_paths_2))
    return text_and_link

def get_text_and_link_from_url_and_urls_and_files_and_files_and_files(url, urls, file_paths_1, file_paths_2, file_paths_3):
    text_and_link = get_text_and_link_from_url(url)
    text_and_link.extend(get_text_and_link_from_urls(urls))
    text_and_link.extend(get_text_and_link_from_files(file_paths_1))
    text_and_link.extend(get_text_and_link_from_files(file_paths_2))
    text_and_link.extend(get_text_and_link_from_files(file_paths_3))
    return text_and_link

def get_text_and_link_from_url_and_urls_and_files_and_files_and_files_and_files(url, urls, file_paths_1, file_paths_2, file_paths_3, file_paths_4):
    text_and_link = get_text_and_link_from_url(url)
    text_and_link.extend(get_text_and_link_from_urls(urls))
    text_and_link.extend(get_text_and_link_from_files(file_paths_1))
    text_and_link.extend(get_text_and_link_from_files(file_paths_2))
    text_and_link.extend(get_text_and_link_from_files(file_paths_3))
    text_and_link.extend(get_text_and_link_from_files(file_paths_4))
    return text_and_link

def get_text_and_link_from_url_and_urls_and_files_and_files_and_files_and_files_and_files(url, urls, file_paths_1, file_paths_2, file_paths_3, file_paths_4, file_paths_5):
    text_and_link = get_text_and_link_from_url(url)
    text_and_link.extend(get_text_and_link_from_urls(urls))
    text_and_link.extend(get_text_and_link_from_files(file_paths_1))
    text_and_link.extend(get_text_and_link_from_files(file_paths_2))
    text_and_link.extend(get_text_and_link_from_files(file_paths_3))
    text_and_link.extend(get_text_and_link_from_files(file_paths_4))
    text_and_link.extend(get_text_and_link_from_files(file_paths_5))
    return text_and_link

def get_text_and_link_from_url_and_urls_and_files_and_files_and_files_and_files_and_files_and_files(url, urls, file_paths_1, file_paths_2, file_paths_3, file_paths_4, file_paths_5, file_paths_6):
    text_and_link = get_text_and_link_from_url(url)
    text_and_link.extend(get_text_and_link_from_urls(urls))
    text_and_link.extend(get_text_and_link_from_files(file_paths_1))
    text_and_link.extend(get_text_and_link_from_files(file_paths_2))
    text_and_link.extend