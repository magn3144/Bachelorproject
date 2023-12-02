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

The task is: Extract the location and wether its a guest favorite ('yes' / 'no') for each Airbnb, and save the two columns as a CSV file.

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

def get_location(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    location = soup.find('span', class_='u17llcap dir dir-ltr').text
    return location

def get_guest_favorite(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    guest_favorite = soup.find('div', class_='t1qa5xaj dir dir-ltr').text
    return guest_favorite

def get_data(html_text):
    location = get_location(html_text)
    guest_favorite = get_guest_favorite(html_text)
    return location, guest_favorite

def get_data_from_url(url):
    html_text = get_html_text(url)
    location, guest_favorite = get_data(html_text)
    return location, guest_favorite

def get_data_from_urls(urls):
    locations = []
    guest_favorites = []
    for url in urls:
        location, guest_favorite = get_data_from_url(url)
        locations.append(location)
        guest_favorites.append(guest_favorite)
    return locations, guest_favorites

def get_urls():
    urls = []
    for i in range(1, 61):
        url = 'https://www.airbnb.com/s/New-York--NY--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=december&flexible_trip_dates%5B%5D=january&flexible_trip_dates%5B%5D=february&date_picker_type=flexible_dates&source=structured_search_input_header&search_type=search_query&checkin=2020-12-28&checkout=2020-01-04&price_min=100&price_max=1000&room_types%5B%5D=Entire%20home%2Fapt&property_type_id%5B%5D=2&property_type_id%5B%5D=3&property_type_id%5B%5D=4&property_type_id%5B%5D=5&property_type_id%5B%5D=6&property_type_id%5B%5D=7&property_type_id%5B%5D=11&property_type_id%5B%5D=12&property_type_id%5B%5D=13&property_type_id%5B%5D=14&property_type_id%5B%5D=15&property_type_id%5B%5D=16&property_type_id%5B%5D=17&property_type_id%5B%5D=18&property_type_id%5B%5D=19&property_type_id%5B%5D=20&property_type_id%5B%5D=21&property_type_id%5B%5D=22&property_type_id%5B%5D=23&property_type_id%5B%5D=24&property_type_id%5B%5D=25&property_type_id%5B%5D=26&property_type_id%5B%5D=27&property_type_id%5B%5D=28&property_type_id%5B%5D=29&property_type_id%5B%5D=30&property_type_id%5B%5D=31&property_type_id%5B%5D=32&property_type_id%5B%5D=33&property_type_id%5B%5D=34&property_type_id%5B%5D=35&property_type_id%5B%5D=36&property_type_id%5B%5D=37&property_type_id%5B%5D=38&property_type_id%5B%5D=39&property_type_id%5B%5D=40&property_type_id%5B%5D=41&property_type_id%5B%5D=42&property_type_id%5B%5D=43&property_type_id%5B%5D=44&property_type_id%5B%5D=45&property_type_id%5B%5D=46&property_type_id%5B%5D=47&property_type_id%5B%5D=48&property_type_id%5B%5D=49&property_type_id%5B%5D=50&property_type_id%5B%5D=51&property_type_id%5B%5D=52&property_type_id%5B%5D=53&property_type_id%5B%5D=54&property_type_id%5B%5D=55&property_type_id%5B%5D=56&property_type_id%5B%5D=57&property_type_id%5B%5D=58&property_type_id%5B%5D=59&property_type_id%5B%5D=60&neighborhood_cleansed%5B%5D=10001&neighborhood_cleansed%5B%5D=10002&neighborhood_cleansed%5B%5D=10003&neighborhood_cleansed%5B%5D=10004&neighborhood_cleansed%5B%5D=10005&neighborhood_cleansed%5B%5D=10006&neighborhood_cleansed%5B%5D=10007&neighborhood_cleansed%5B%5D=10008&neighborhood_cleansed%5B%5D=10009&neighborhood_cleansed%5B%5D=10010&neighborhood_cleansed%5B%5D=10011&neighborhood_cleansed%5B%5D=10012&neighborhood_cleansed%5B%5D=10013&neighborhood_cleansed%5B%5D=10014&neighborhood_cleansed%5B%5D=10015&neighborhood_cleansed%5B%5D=10016&neighborhood_cleansed%5B%5D=10017&neighborhood_cleansed%5B%5D=10018&neighborhood_cleansed%5B%5D=10019&neighborhood_cleansed%5B%5D=10020&neighborhood_cleansed%5B%5D=10021&neighborhood_cleansed%5B%5D=10022&neighborhood_cleansed%5B%5D=10023&neighborhood_cleansed%5B%5D=10024&neighborhood_cleansed%5B%5D=10025&neighborhood_cleansed%5B%5D=10026&neighborhood_cleansed%5B%5D=10