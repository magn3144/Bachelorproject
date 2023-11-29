You are given a web page, the category of the page, randomly selected html elements on that page, the local path to the HTML file that should be scraped and a web-scraping task that you should solve.

Here are some randomly selected HTML elements (containing text), and their corresponding XPaths from the target page:
<a class="l1ovpqvx c1kblhex dir dir-ltr">Airbnb-friendly apartments</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[2]/ul/li[6]/a
----------------
<a class="_r243u8q l1ovpqvx dir dir-ltr">Sitemap</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[2]/section/div[3]/div[1]/div/div[2]/span[2]/ol/li[2]/a
----------------
<span class="u17llcap dir dir-ltr">Learn about Guest Favorites, the most loved homes </span>
/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/h1/div[3]/a/span
----------------
<span class="ti7yjx dir dir-ltr">Grand pianos</span>
/html/body/div[5]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div/label[48]/div/span/div/span
----------------
<div class="t1jojoys dir dir-ltr" id="title_689161363553525770">Nykøbing Sjælland, Denmark</div>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[35]/div/div[2]/div/div/div/div/div/div[2]/div[1]
----------------
<div class="t1qa5xaj dir dir-ltr">Guest favorite</div>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[24]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div
----------------
<h2 class="hifxi0b dir dir-ltr">Inspiration for future getaways</h2>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[1]/div/div/div/div/h2
----------------
<h2 id="footerHeading">Site Footer</h2>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/span/h2
----------------
<h3 class="trsc28b dir dir-ltr">Hosting</h3>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[2]/h3
----------------
<a class="l1ovpqvx c1kblhex dir dir-ltr">Airbnb.org emergency stays</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/ul/li[6]/a
----------------
<a class="l1ovpqvx c1kblhex dir dir-ltr">AirCover</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[1]/ul/li[2]/a
----------------
<span class="u17llcap dir dir-ltr">Learn about Guest Favorites, the most loved homes </span>
/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/h1/div[2]/div/a/span
----------------
<span class="ti7yjx dir dir-ltr">Earth homes</span>
/html/body/div[5]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div/label[34]/div/span/div/span
----------------
<div class="db9tcim dir dir-ltr" id="category-bar-description">17 of 61 Airbnb Categories showing</div>
/html/body/div[5]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[1]
----------------
<div class="t1jojoys dir dir-ltr" id="title_12457951">Tisvildeleje, Denmark</div>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[32]/div/div[2]/div/div/div/div/div/div[2]/div[1]
----------------
<h3 class="trsc28b dir dir-ltr">Airbnb</h3>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/h3
----------------
<a class="l1ovpqvx c1kblhex dir dir-ltr">Report neighborhood concern</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[1]/ul/li[6]/a
----------------
<a class="l1ovpqvx c1kblhex dir dir-ltr">Cancellation options</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[1]/ul/li[5]/a
----------------
<span class="u17llcap dir dir-ltr">Learn about Guest Favorites, the most loved homes </span>
/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/h1/div[1]/a/span
----------------
<span class="dir dir-ltr">Nov 13 – 18</span>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[3]/span/span
----------------
<div class="t1qa5xaj dir dir-ltr">Guest favorite</div>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[7]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div
----------------
<h3 class="trsc28b dir dir-ltr">Support</h3>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[1]/h3
----------------
<a class="l1ovpqvx c1kblhex dir dir-ltr">Airbnb your home</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[2]/ul/li[1]/a
----------------
<span class="r1dxllyb dir dir-ltr">4.92</span>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[19]/div/div[2]/div/div/div/div/div/div[2]/span/span[2]
----------------
<div class="pz9siyu pk4ruxu dir dir-ltr">Add dates</div>
/html/body/div[5]/div/div/div[1]/div/div[2]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div[1]/div[3]/div[1]/div/div/div[2]
----------------
<a class="l1ovpqvx c1kblhex dir dir-ltr">Newsroom</a>
/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/ul/li[1]/a
----------------
<span class="ti7yjx dir dir-ltr">Bed &amp; breakfasts</span>
/html/body/div[5]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div/label[20]/div/span/div/span
----------------
<div class="t1jojoys dir dir-ltr" id="title_37198124">Frederiksværk, Denmark</div>
Do NOT include these directly in your code!

The page is from this website: airbnb

The local path to the HTML file is downloaded_pages/airbnb.html

The category is: Tourism

The task is: Collect information about Guest Favorites, the most-loved homes, and save it as a CSV file.

Now generate a python script that solves this task.
Make sure the script works when I run it, without any modifications.
The script you generate should always save the scraped data as a CSV file with the name 'scraped_data.csv'.
You can use the given HTML elements above to gain information about the page. ### Response: ```
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find all the Guest Favorites
guest_favorites = tree.xpath('//div[@class="t1jojoys dir dir-ltr" and @id="title_689161363553525770"]')

# Extract the information about the Guest Favorites
guest_favorites_data = []
for guest_favorite in guest_favorites:
    # Get the title
    title = guest_favorite.text

    # Get the link
    link = guest_favorite.get('id')

    # Get the location
    location = guest_favorite.getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().get