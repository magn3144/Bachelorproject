You are given a web page, the category of the page, randomly selected html elements on that page, the local path to the HTML file that should be scraped and a web-scraping task that you should solve.

Here are some randomly selected HTML elements (containing text), and their corresponding XPaths from the target page:
<span class="ipc-rating-star--rate">Rate</span>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[207]/div[2]/div/div/span/div/button/span/span
----------------
<div class="sc-bb1bba6c-1 ipcpFw news-preview-card-articleTitle">Marvel Delays ‘Deadpool 3,’ ‘Captain America 4’ an</div>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[2]/div/div/div[1]/div
----------------
<div class="ipc-title__description">From the past weekend</div>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[4]/div[2]/div
----------------
<h3 class="ipc-title__text">136. Judgment at Nuremberg</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[136]/div[2]/div/div/div[1]/a/h3
----------------
<h3 class="ipc-title__text">55. Apocalypse Now</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[55]/div[2]/div/div/div[1]/a/h3
----------------
<h1 class="ipc-title__text chart-layout-specific-title-text">IMDb Top 250 Movies</h1>
/html/body/div[2]/main/div/div[3]/section/div/div[1]/div/div[2]/hgroup/h1
----------------
<label class="ipc-simple-select__front-label">Sort by</label>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[3]/div/span/label
----------------
<p>The Top Rated Movie list only includes feature fil</p>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/p
----------------
<li>The list is ranked by a formula which includes the</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/ul/li[2]
----------------
<li class="ipc-inline-list__item">by J. Kim Murphy</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[2]/div/div/div[1]/ul/li[2]
----------------
<a class="ipc-link ipc-link--base">Learn more about how list ranking is determined.</a>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/a
----------------
<a class="ipc-link ipc-link--baseAlt ipc-link--touch-target ipc-link--inherit-color">Your Ads Privacy Choices</a>
/html/body/div[2]/footer/div[3]/div[1]/div[3]/ul/li[6]/div/a[2]
----------------
<title>IMDb, an Amazon company</title>
/html/body/div[2]/footer/div[3]/div[2]/svg/title
----------------
<span class="sc-c7e5f54-8 fiTXuB cli-title-metadata-item">1997</span>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[179]/div[2]/div/div/div[2]/span[1]
----------------
<div class="sc-bb1bba6c-1 ipcpFw news-preview-card-articleTitle">Elon Musk Biopic in the Works at A24 With Darren A</div>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[4]/div/div/div[1]/div
----------------
<div class="navlsl__itemTitle navlsl_icon">Language</div>
/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/label/span/li/span[1]/div[1]
----------------
<h3 class="ipc-title__text">66. Witness for the Prosecution</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[66]/div[2]/div/div/div[1]/a/h3
----------------
<h3 class="ipc-title__text">200. Mad Max: Fury Road</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[200]/div[2]/div/div/div[1]/a/h3
----------------
<label class="ipc-boolean-input__label">Hide titles you've rated</label>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[2]/span/div/span/div/span/label
----------------
<li>To be included on the list, a movie must receive r</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/ul/li[3]
----------------
<li class="ipc-inline-list__item">by Clayton Davis</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[5]/div/div/div[1]/ul/li[2]
----------------
<a class="ipc-link ipc-link--baseAlt ipc-link--touch-target ipc-link--inherit-color">Privacy Policy</a>
/html/body/div[2]/footer/div[3]/div[1]/div[3]/ul/li[5]/a
----------------
<span class="ipc-rating-star--voteCount"> (540K)</span>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[168]/div[2]/div/div/span/div/span/span
----------------
<div class="sc-bb1bba6c-1 ipcpFw news-preview-card-articleTitle">Ariana DeBose Breaks Down Her Emotional ‘Wish’ Per</div>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[1]/div/div/div[1]/div
----------------
<div class="navlsl__itemContent">English (United States)</div>
/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/label/span/li/span[1]/div[2]
----------------
<h3 class="ipc-title__text">9. The Lord of the Rings: The Fellowship of the Ri</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[9]/div[2]/div/div/div[1]/a/h3
----------------
<h3 class="ipc-title__text">154. Finding Nemo</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[154]/div[2]/div/div/div[1]/a/h3
----------------
<label class="ipc-simple-select__selected-option">Ranking</label>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[3]/div/span/span/label
----------------
<li>Shorts, TV movies, and documentaries are not inclu</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/ul/li[1]
----------------
<li class="ipc-inline-list__item">11/10/2023</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[3]/div/div/div[1]/ul/li[1]
----------------
<a class="ipc-link ipc-link--baseAlt ipc-link--touch-target ipc-link--inherit-color">Conditions of Use</a>
/html/body/div[2]/footer/div[3]/div[1]/div[3]/ul/li[4]/a
----------------
<span class="sc-c7e5f54-8 fiTXuB cli-title-metadata-item">12A</span>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[205]/div[2]/div/div/div[2]/span[3]
----------------
<div class="sc-iBzDrC iRtuib">For Industry Professionals</div>
/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/a/span[1]/div/div
----------------
<h3 class="ipc-title__text">228. Pirates of the Caribbean: The Curse of the Bl</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[228]/div[2]/div/div/div[1]/a/h3
----------------
<h3 class="ipc-title__text">IMDb Charts</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[1]/div/div[1]/div[1]/hgroup/h3
----------------
<li class="ipc-inline-list__item">by Jazz Tangcay</li>
Do NOT include these directly in your code!

The page is from this website: imdb

The local path to the HTML file is downloaded_pages/imdb.html

The category is: Forums and Review Sites

The task is: Generate a list of web-scraping tasks:

Now generate a python script that solves this task.
Make sure the script works when I run it, without any modifications.
The script you generate should always save the scraped data as a CSV file with the name 'scraped_data.csv'.
You can use the given HTML elements above to gain information about the page. ### Response: ```

You are given a web page, the category of the page, randomly selected html elements on that page, the local path to the HTML file that should be scraped and a web-scraping task that you should solve.

Here are some randomly selected HTML elements (containing text), and their corresponding XPaths from the target page:
<span class="ipc-rating-star--rate">Rate</span>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[2]/div/div/div[1]/button/span/span
----------------
<div class="sc-bb1bba6c-1 ipcpFw news-preview-card-articleTitle">Ariana DeBose Breaks Down Her Emotional ‘Wish’ Perf</div>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[1]/div/div/div[1]/div
----------------
<div class="navlsl__itemTitle navlsl_icon">Language</div>
/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/label/span/li/span[1]/div[2]
----------------
<h3 class="ipc-title__text">10. The Lion King</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[10]/div[2]/div/div/div[1]/a/h3
----------------
<h3 class="ipc-title__text">11. The Godfather</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[11]/div[2]/div/div/div[1]/a/h3
----------------
<label class="ipc-boolean-input__label">Hide titles you've rated</label>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[2]/span/div/span/div/span/label
----------------
<li>To be included on the list, a movie must receive r</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/ul/li[3]
----------------
<li class="ipc-inline-list__item">by Clayton Davis</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[5]/div/div/div[1]/ul/li[2]
----------------
<a class="ipc-link ipc-link--baseAlt ipc-link--touch-target ipc-link--inherit-color">Privacy Policy</a>
/html/body/footer/div[1]/div[2]/div[3]/ul/li[5]/a
----------------
<span class="ipc-rating-star--voteCount"> (540K)</span>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[168]/div[2]/div/div/span/div/span/span
----------------
<div class="sc-bb1bba6c-1 ipcpFw news-preview-card-articleTitle">Ariana DeBose Breaks Down Her Emotional ‘Wish’ Perf</div>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[2]/div/div/div[1]/div
----------------
<div class="navlsl__itemContent">English (United States)</div>
/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/label/span/li/span[1]/div[2]
----------------
<h3 class="ipc-title__text">17. The Silence of the Lambs</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[17]/div[2]/div/div/div[1]/a/h3
----------------
<h3 class="ipc-title__text">18. Schindler's List</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[18]/div[2]/div/div/div[1]/a/h3
----------------
<label class="ipc-simple-select__selected-option">Ranking</label>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[3]/div/span/span/label
----------------
<li>Shorts, TV movies, and documentaries are not inclu</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/ul/li[1]
----------------
<li class="ipc-inline-list__item">11/10/2023</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[3]/div/div/div[1]/ul/li[1]
----------------
<a class="ipc-link ipc-link--baseAlt ipc-link--touch-target ipc-link--inherit-color">Conditions of Use</a>
/html/body/footer/div[1]/div[2]/div[3]/ul/li[4]/a
----------------
<span class="sc-c7e5f54-8 fiTXuB cli-title-metadata-item">1997</span>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[179]/div[2]/div/div/div[2]/span[1]
----------------
<div class="sc-bb1bba6c-1 ipcpFw news-preview-card-articleTitle">Elon Musk Biopic in the Works at A24 With Darren A</div>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[4]/div/div/div[1]/div
----------------
<div class="navlsl__itemTitle navlsl_icon">Language</div>
/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/label/span/li/span[1]/div[1]
----------------
<h3 class="ipc-title__text">9. The Lord of the Rings: The Fellowship of the Ri</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[9]/div[2]/div/div/div[1]/a/h3
----------------
<h3 class="ipc-title__text">154. Finding Nemo</h3>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[154]/div[2]/div/div/div[1]/a/h3
----------------
<label class="ipc-simple-select__selected-option">Ranking</label>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[3]/div/span/span/label
----------------
<li>Shorts, TV movies, and documentaries are not inclu</li>
/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/ul/li[1]
----------------
<li class="ipc-inline-list__item">by Jazz Tangcay</li>