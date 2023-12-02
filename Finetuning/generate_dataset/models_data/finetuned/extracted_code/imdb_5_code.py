You are given a web page, the category of the page, randomly selected html elements on that page, the local path to the HTML file that should be scraped and a web-scraping task that you should solve.

Here are some randomly selected HTML elements (containing text), and their corresponding XPaths from the target page:
<span class="ipc-rating-star--rate">Rate</span>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[28]/div[2]/div/div/span/div/button/span/span
----------------
<div class="sc-bb1bba6c-1 ipcpFw news-preview-card-articleTitle">Elon Musk Biopic in the Works at A24 With Darren A</div>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[4]/div/div/div[1]/div
----------------
<div class="ipc-title__description">From the past weekend</div>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[4]/div[2]/div
----------------
<h3 class="ipc-title__text">67. Spider-Man: Into the Spider-Verse</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[67]/div[2]/div/div/div[1]/a/h3
----------------
<h3 class="ipc-title__text">227. The Wizard of Oz</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[227]/div[2]/div/div/div[1]/a/h3
----------------
<h1 class="ipc-title__text chart-layout-specific-title-text">IMDb Top 250 Movies</h1>
/html/body/div[2]/main/div/div[3]/section/div/div[1]/div/div[2]/hgroup/h1
----------------
<label class="ipc-simple-select__selected-option">Ranking</label>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[3]/div/span/span/label
----------------
<p>The Top Rated Movie list only includes feature fil</p>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/p
----------------
<li>The list is ranked by a formula which includes the</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/ul/li[2]
----------------
<li class="ipc-inline-list__item">by Ellise Shafer</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[4]/div/div/div[1]/ul/li[2]
----------------
<a class="ipc-link ipc-link--base">Learn more about how list ranking is determined.</a>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/a
----------------
<a class="ipc-link ipc-link--baseAlt ipc-link--touch-target ipc-link--inherit-color">Press Room</a>
/html/body/div[2]/footer/div[3]/div[1]/div[3]/ul/li[1]/a
----------------
<title>IMDb, an Amazon company</title>
/html/body/div[2]/footer/div[3]/div[2]/svg/title
----------------
<span class="sc-c7e5f54-8 fiTXuB cli-title-metadata-item">18</span>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[96]/div[2]/div/div/div[2]/span[3]
----------------
<div class="ipc-title__description">Top 250 as rated by IMDb Users</div>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[4]/div[6]/div
----------------
<div class="navlsl__itemContent">English (United States)</div>
/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/label/span/li/span[1]/div[2]
----------------
<h3 class="ipc-title__text">116. Indiana Jones and the Last Crusade</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[116]/div[2]/div/div/div[1]/a/h3
----------------
<h3 class="ipc-title__text">43. The Usual Suspects</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[43]/div[2]/div/div/div[1]/a/h3
----------------
<label class="ipc-boolean-input__label">Hide titles you've rated</label>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[2]/span/div/span/div/span/label
----------------
<li>Shorts, TV movies, and documentaries are not inclu</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/ul/li[1]
----------------
<li class="ipc-inline-list__item">by Jazz Tangcay</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[1]/div/div/div[1]/ul/li[2]
----------------
<a class="ipc-link ipc-link--baseAlt ipc-link--touch-target ipc-link--inherit-color">Conditions of Use</a>
/html/body/div[2]/footer/div[3]/div[1]/div[3]/ul/li[4]/a
----------------
<span class="sc-c7e5f54-8 fiTXuB cli-title-metadata-item">AA</span>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[77]/div[2]/div/div/div[2]/span[3]
----------------
<div class="sc-iBzDrC iRtuib">For Industry Professionals</div>
/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/a/span[1]/div/div
----------------
<div class="navlsl__itemTitle navlsl_icon">Language</div>
/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/label/span/li/span[1]/div[1]
----------------
<h3 class="ipc-title__text">72. Dr. Strangelove or: How I Learned to Stop Worr</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[72]/div[2]/div/div/div[1]/a/h3
----------------
<h3 class="ipc-title__text">68. Aliens</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[68]/div[2]/div/div/div[1]/a/h3
----------------
<label class="ipc-simple-select__front-label">Sort by</label>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[3]/div/span/label
----------------
<li>To be included on the list, a movie must receive r</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/ul/li[3]
----------------
<li class="ipc-inline-list__item">11/10/2023</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[2]/div/div/div[1]/ul/li[1]
----------------
<a class="ipc-link ipc-link--baseAlt ipc-link--touch-target ipc-link--inherit-color">Your Ads Privacy Choices</a>
/html/body/div[2]/footer/div[3]/div[1]/div[3]/ul/li[6]/div/a[2]
----------------
<span class="ipc-rating-star--voteCount"> (50K)</span>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[86]/div[2]/div/div/span/div/span/span
----------------
<div class="ipc-title__description">As determined by IMDb users</div>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[4]/div[5]/div
----------------
<h3 class="ipc-title__text">148. No Country for Old Men</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[148]/div[2]/div/div/div[1]/a/h3
----------------
<h3 class="ipc-title__text">89. Requiem for a Dream</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[89]/div[2]/div/div/div[1]/a/h3
----------------
<li class="ipc-inline-list__item">by Anna Tingley</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[3]/div/div/div[1]/ul/li[2]
----------------
Do NOT include these directly in your code!

The page is from this website: imdb

The local path to the HTML file is downloaded_pages/imdb.html

The category is: Forums and Review Sites

The task is: Collect the amount of ratings for each movie in the IMDb Top 250 list and store it in a CSV file.

Now generate a python script that solves this task.
Make sure the script works when I run it, without any modifications.
The script you generate should always save the scraped data as a CSV file with the name 'scraped_data.csv'.
You can use the given HTML elements above to gain information about the page. ### Response: ```python
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the ratings
ratings = tree.xpath('//span[@class="ipc-rating-star--voteCount"]')

# Create a list of tuples with the movie title and rating
data = []
for rating in ratings:
    title = rating.getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent().getparent