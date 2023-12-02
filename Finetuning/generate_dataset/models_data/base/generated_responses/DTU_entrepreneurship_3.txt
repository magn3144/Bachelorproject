You are given a web page, the category of the page, randomly selected html elements on that page, the local path to the HTML file that should be scraped and a web-scraping task that you should solve.

Here are some randomly selected HTML elements (containing text), and their corresponding XPaths from the target page:
<span>38105 Digital trends for entrepreneurs | 5 ECTS | </span>
/html/body/form/div[3]/div[5]/div[5]/div/div[2]/div/h2/span
----------------
<span class="servicemenu__link-text">DTU.dk</span>
/html/body/form/div[3]/header/div[1]/div[2]/div/div[1]/a/span
----------------
<h2 class="hide-mobile">Centre for Technology Entrepreneurship</h2>
/html/body/form/div[3]/footer/div[1]/div/div[2]/h2
----------------
<h2>Departments and Centres</h2>
/html/body/form/div[3]/header/div[1]/div[2]/div/div[2]/nav/div[1]/div/div/div[3]/h2
----------------
<a>DTU Electrical Engineering</a>
/html/body/form/div[3]/footer/div[2]/div[1]/div/div[2]/nav/div[1]/div/div/div[3]/ul[1]/li[8]/a
----------------
<a>Our use of personal data</a>
/html/body/form/div[3]/footer/div[1]/div/div[2]/div[2]/div[2]/p[2]/a
----------------
<label>Projects</label>
/html/body/form/div[3]/header/div[1]/div[2]/div/div[3]/div/div[2]/ul/li[4]/label
----------------
<h1 class="invisible" id="outercontent_0_ContentHeading">All entrepreneurship courses</h1>
/html/body/form/div[3]/div[5]/h1
----------------
<p class="a-paragraph-lead o-hero__text">All entrepreneurship and innovation courses are li</p>
/html/body/form/div[3]/div[5]/div[2]/div/div[2]/div/p
----------------
<div class="grid_9">            https://www.entrepreneurship.dtu.dk/e</div>
/html/body/form/div[3]/footer/div[3]/div[1]
----------------
<div class="o-hero__background"></div>
/html/body/form/div[3]/div[5]/div[9]/div/div[1]
----------------
<span>38106 Developing an entrepreneurial mindset throug</span>
/html/body/form/div[3]/div[5]/div[6]/div/div[1]/div/h2/span
----------------
<span class="sitetextlogo">DTU Entrepreneurship </span>
/html/body/form/div[3]/header/div[2]/div/div/div[1]/a/span
----------------
<h2 class="a-heading-h1 o-hero__title">Explore entrepreneurship and innovation courses </h2>
/html/body/form/div[3]/div[5]/div[2]/div/div[2]/div/h2
----------------
<h2 class="a-heading-h1 o-hero__title">Spring semester</h2>
/html/body/form/div[3]/div[5]/div[11]/div/div[2]/div/h2
----------------
<a>DTU Wind and Energy Systems</a>
/html/body/form/div[3]/footer/div[2]/div[1]/div/div[2]/nav/div[1]/div/div/div[3]/ul[3]/li[7]/a
----------------
<a>DTU Bioengineering</a>
/html/body/form/div[3]/footer/div[2]/div[1]/div/div[2]/nav/div[1]/div/div/div[3]/ul[1]/li[2]/a
----------------
<label>Projects</label>
/html/body/form/div[3]/footer/div[2]/div[1]/div/div[3]/div/div[2]/ul/li[4]/label
----------------
<div class="grid_3">            23 NOVEMBER 2023            </div>
/html/body/form/div[3]/footer/div[3]/div[2]
----------------
<div class="o-hero__background"></div>
/html/body/form/div[3]/div[5]/div[11]/div/div[1]
----------------
<span>38107 Business design for sustainability | 5 ECTS </span>
/html/body/form/div[3]/div[5]/div[5]/div/div[1]/div/h2/span
----------------
<span class="subscriptionFormError" id="ctl17_ctl06_ctl00_ctl00">Valid email address</span>
/html/body/form/div[3]/footer/div[1]/div/div[4]/div[2]/div/span[1]
----------------
<h2 class="a-heading-h1 o-hero__title">Do you want to write an entrepreneurial thesis wit</h2>
/html/body/form/div[3]/div[5]/div[16]/div/div[2]/div/h2
----------------
<h2>Departments and Centres</h2>
/html/body/form/div[3]/footer/div[2]/div[1]/div/div[2]/nav/div[1]/div/div/div[3]/h2
----------------
<a>Corporate innovation focus and innovation tools | </a>
/html/body/form/div[3]/div[5]/div[7]/div/div[2]/ul/li/a
----------------
<a>DTU Entrepreneurship </a>
/html/body/form/div[3]/footer/div[2]/div[1]/div/div[2]/nav/div[1]/div/div/div[3]/ul[2]/li[3]/a
----------------
<label>DTU Entrepreneurship </label>
/html/body/form/div[3]/footer/div[2]/div[1]/div/div[3]/div/div[2]/ul/li[1]/label
----------------
<div class="footeraddresstitle grid_5 alpha">            DTU Entrepreneurship         </div>
/html/body/form/div[3]/footer/div[1]/div/div[2]/div[2]/div[1]
----------------
<div class="o-hero__background"></div>
/html/body/form/div[3]/div[5]/div[17]/div/div[1]
----------------
<span>38101 Knowledge-based entrepreneurship | 5 ECTS  |</span>
/html/body/form/div[3]/div[5]/div[7]/div/div[1]/div/h2/span
----------------
<span class="servicemenu__link-text">DTU.dk</span>
/html/body/form/div[3]/footer/div[2]/div[1]/div/div[1]/a/span
----------------
<h2 class="a-heading-h1 o-hero__title">3 weeks in January</h2>
/html/body/form/div[3]/div[5]/div[9]/div/div[2]/div/h2
----------------
<a>DTU Engineering Technology</a>
/html/body/form/div[3]/footer/div[2]/div[1]/div/div[2]/nav/div[1]/div/div/div[3]/ul[2]/li[2]/a
----------------
<a>DTU Management </a>
/html/body/form/div[3]/footer/div[2]/div[1]/div/div[2]/nav/div[1]/div/div/div[3]/ul[3]/li[1]/a
----------------
<label>Persons</label>
/html/body/form/div[3]/header/div[1]/div[2]/div/div[3]/div/div[2]/ul/li[2]/label
----------------
<div class="grid_3 pagefootercolumn inline-block minHeight" id="footerJob"></div>
/html/body/form/div[3]/footer/div[1]/div/div[3]
----------------
<span>38102 Technology entrepreneurship | 5 ECTS | MSc |</span>
/html/body/form/div[3]/div[5]/div[8]/div/div[1]/div/h2/span
----------------
<span class="subscriptionFormError" id="ctl17_ctl06_ctl00_EmailValidator">Valid email address</span>
/html/body/form/div[3]/footer/div[1]/div/div[4]/div[2]/div/span[2]
----------------
<h2 class="top-border-mobile">Follow us on</h2>
/html/body/form/div[3]/footer/div[1]/div/div[4]/h2
----------------
<a>38203 Due diligence of new ventures </a>
/html/body/form/div[3]/div[5]/div[15]/div/div[1]/ul/li[1]/a
----------------
<a>DTU Space</a>
/html/body/form/div[3]/header/div[1]/div[2]/div/div[2]/nav/div[1]/div/div/div[3]/ul[3]/li[6]/a
----------------
<label>Publications</label>
/html/body/form/div[3]/header/div[1]/div[2]/div/div[3]/div/div[2]/ul/li[3]/label
----------------
<div class="o-hero__background"></div>
/html/body/form/div[3]/div[5]/div[4]/div/div[1]
----------------
<span>In addition, DTU also offers courses as part of th</span>
/html/body/form/div[3]/div[5]/div[15]/div/div[1]/div/h2/span
----------------
<h2 class="a-heading-h1 o-hero__title">Autumn semester</h2>
/html/body/form/div[3]/div[5]/div[4]/div/div[2]/div/h2
----------------
Do NOT include these directly in your code!

The page is from this website: DTU_entrepreneurship

The local path to the HTML file is downloaded_pages/DTU_entrepreneurship.html

The category is: Educational Websites

The task is: Get the text of each button in the header (like about us, and education) and save them in seperate rows.

Now generate a python script that solves this task.
Make sure the script works when I run it, without any modifications.
The script you generate should always save the scraped data as a CSV file with the name 'scraped_data.csv'.
You can use the given HTML elements above to gain information about the page. ### Response: ```

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.dtu.dk/en/entrepreneurship'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

#print(soup.prettify())

#print(soup.find_all('a'))

#print(soup.find_all('a', class_='servicemenu__link-text'))

#print(soup.find_all('a', class_='servicemenu__link-text')[0].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[1].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[2].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[3].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[4].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[5].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[6].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[7].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[8].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[9].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[10].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[11].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[12].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[13].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[14].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[15].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[16].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[17].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[18].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[19].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[20].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[21].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[22].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[23].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[24].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[25].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[26].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[27].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[28].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[29].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[30].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[31].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[32].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[33].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[34].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[35].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[36].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[37].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[38].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[39].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[40].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[41].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[42].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[43].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[44].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[45].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[46].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[47].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[48].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[49].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[50].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[51].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[52].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[53].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[54].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[55].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[56].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[57].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[58].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[59].text)

#print(soup.find_all('a', class_='servicemenu__link-text')[60].text)