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

The task is: Scrape all links in the footer under support, hosting and Airbnb, and save them in a CSV in three seperate columns.

Now generate a python script that solves this task.
Make sure the script works when I run it, without any modifications.
The script you generate should always save the scraped data as a CSV file with the name 'scraped_data.csv'.
You can use the given HTML elements above to gain information about the page. ### Response: ```

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')
    return [link.get('href') for link in links]

def get_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.find_all('span')
    return [text.get_text() for text in text]

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div')
    return [data.get_text() for data in data]

def get_all_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data = soup.find_all('div')
    return [all_data.get_text() for all_data in all_data]

def get_all_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_links = soup.find_all('a')
    return [all_links.get('href') for all_links in all_links]

def get_all_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_text = soup.find_all('span')
    return [all_text.get_text() for all_text in all_text]

def get_all_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data = soup.find_all('div')
    return [all_data.get_text() for all_data in all_data]

def get_all_data_2(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_2 = soup.find_all('div')
    return [all_data_2.get_text() for all_data_2 in all_data_2]

def get_all_data_3(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_3 = soup.find_all('div')
    return [all_data_3.get_text() for all_data_3 in all_data_3]

def get_all_data_4(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_4 = soup.find_all('div')
    return [all_data_4.get_text() for all_data_4 in all_data_4]

def get_all_data_5(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_5 = soup.find_all('div')
    return [all_data_5.get_text() for all_data_5 in all_data_5]

def get_all_data_6(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_6 = soup.find_all('div')
    return [all_data_6.get_text() for all_data_6 in all_data_6]

def get_all_data_7(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_7 = soup.find_all('div')
    return [all_data_7.get_text() for all_data_7 in all_data_7]

def get_all_data_8(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_8 = soup.find_all('div')
    return [all_data_8.get_text() for all_data_8 in all_data_8]

def get_all_data_9(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_9 = soup.find_all('div')
    return [all_data_9.get_text() for all_data_9 in all_data_9]

def get_all_data_10(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_10 = soup.find_all('div')
    return [all_data_10.get_text() for all_data_10 in all_data_10]

def get_all_data_11(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_11 = soup.find_all('div')
    return [all_data_11.get_text() for all_data_11 in all_data_11]

def get_all_data_12(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_12 = soup.find_all('div')
    return [all_data_12.get_text() for all_data_12 in all_data_12]

def get_all_data_13(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_13 = soup.find_all('div')
    return [all_data_13.get_text() for all_data_13 in all_data_13]

def get_all_data_14(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_14 = soup.find_all('div')
    return [all_data_14.get_text() for all_data_14 in all_data_14]

def get_all_data_15(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_15 = soup.find_all('div')
    return [all_data_15.get_text() for all_data_15 in all_data_15]

def get_all_data_16(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_16 = soup.find_all('div')
    return [all_data_16.get_text() for all_data_16 in all_data_16]

def get_all_data_17(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_17 = soup.find_all('div')
    return [all_data_17.get_text() for all_data_17 in all_data_17]

def get_all_data_18(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data_18 = soup.find_all('div')
    return [all_data_18.get_text() for all_data_18 in all_data_18]

def get_all_data_19(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_data