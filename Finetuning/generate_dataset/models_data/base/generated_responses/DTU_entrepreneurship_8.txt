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

The task is: Save the description of DTU entrepreneourship, which is under the header "CENTRE FOR TECHNOLOGY ENTREPRENEURSHIP".

Now generate a python script that solves this task.
Make sure the script works when I run it, without any modifications.
The script you generate should always save the scraped data as a CSV file with the name 'scraped_data.csv'.
You can use the given HTML elements above to gain information about the page. ### Response: ```

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = 'https://www.dtu.dk/en/entrepreneurship'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

#print(soup.prettify())

#print(soup.find_all('div', class_='o-hero__background'))

#print(soup.find_all('div', class_='o-hero__background')[0])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style'))

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' '))

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"'))

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0].split('"')[1])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0].split('"')[1].split('"'))

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0].split('"')[1].split('"')[0])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0].split('"')[1].split('"')[0].split('"'))

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0].split('"')[1].split('"')[0].split('"')[0])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0].split('"')[1].split('"')[0].split('"')[0].split('"'))

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0].split('"')[1].split('"')[0].split('"')[0].split('"')[0])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0].split('"')[1].split('"')[0].split('"')[0].split('"')[0].split('"'))

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0].split('"')[1].split('"')[0].split('"')[0].split('"')[0].split('"')[0])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0].split('"')[1].split('"')[0].split('"')[0].split('"')[0].split('"')[0].split('"'))

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0].split('"')[1].split('"')[0].split('"')[0].split('"')[0].split('"')[0].split('"')[0])

#print(soup.find_all('div', class_='o-hero__background')[0].get('style').split(' ')[1].split(':')[1].split(';')[0].split('"')[1].split('"')[0].split('(')[1].split(')')[0].split(',')[0].split('"')[1].split('"')[0].split('"')[0].split('"')[0].split('"')[0].split('"')[0].split('"'))

#print(soup.find_