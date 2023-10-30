import csv
from bs4 import BeautifulSoup

# Define the target HTML file path
html_file = 'downloaded_pages/bloggersroad.html'

# Define the category
category = 'Blogs'

# Define the task: extracting author names and their XPaths
task = 'Extract the author names and their XPaths'

# Define the list of HTML elements and their corresponding XPaths
html_elements = [
    ('<a>10 Things You Must Know Before Buying Exquisite Te</a>', '/html/body/div/div[1]/div/main/div/article[2]/div/header/h2/a'),
    ('<a>Business</a>', '/html/body/div/header/div[2]/div/div/nav/ul/li[2]/a'),
    ('<p> Make an statement by purchasing white clothes: </p>', '/html/body/div/div[1]/section/section[5]/div/div/p'),
    ('<span class="screen-reader-text">Search for:</span>', '/html/body/div/div[1]/section/section[3]/form/label/span'),
    ('<h2 class="screen-reader-text">Posts navigation</h2>', '/html/body/div/div[1]/div/main/nav/h2'),
    ('<h4 class="widget-title">Recent Posts</h4>', '/html/body/div/div[1]/section/section[4]/h4'),
    ('<a>Best Free Classifieds in Henderson, Nevada</a>', '/html/body/div/div[1]/div/main/div/article[3]/div/header/h2/a'),
    ('<a>Shopping</a>', '/html/body/div/header/div[2]/div/div/nav/ul/li[4]/a'),
    ('<p>Are you a tea enthusiast who revels in the art of </p>', '/html/body/div/div[1]/div/main/div/article[2]/div/div/p'),
    ('<span class="page-numbers current">1</span>', '/html/body/div/div[1]/div/main/nav/div/span[1]'),
    ('<h4 class="widget-title">Online Shopping</h4>', '/html/body/div/div[1]/section/section[5]/h4'),
    ('<a>A Stylish Collection for Him: Unraveling Exquisite</a>', '/html/body/div/div[1]/div/main/div/article[1]/div/header/h2/a'),
    ('<a class="url fn n">admin</a>', '/html/body/div/div[1]/div/main/div/article[2]/div/header/div/span[2]/span/a'),
    ('<p>Henderson, Nevada, is a vibrant and dynamic commun</p>', '/html/body/div/div[1]/div/main/div/article[3]/div/div/p'),
    ('<span class="screen-reader-text">Next Posts</span>»', '/html/body/div/div[1]/div/main/nav/div/a[4]/span'),
    ('<a>Craigslist Alternative Classifieds in Greensboro, </a>', '/html/body/div/div[1]/div/main/div/article[4]/div/header/h2/a'),
    ('<a>Business</a>,', '/html/body/div/div[1]/div/main/div/article[3]/footer/div[1]/a[1]'),
    ('<p>Discover a fashionable world of accessories crafte</p>', '/html/body/div/div[1]/div/main/div/article[1]/div/div/p'),
    ('<span class="screen-reader-text">Search</span>', '/html/body/div/div[1]/section/section[3]/form/button/span'),
    ('<a>10 Things You Must Know Before Buying Exquisite Te</a>', '/html/body/div/div[1]/section/section[4]/ul/li[2]/a'),
    ('<a class="page-numbers">2</a>', '/html/body/div/div[1]/div/main/nav/div/a[1]'),
    ('<p class="site-description">Blog Posts on Technology, Marketing, and Much More</p>', '/html/body/div/header/div[1]/div/p'),
    ('<span class="page-numbers dots">…</span>', '/html/body/div/div[1]/div/main/nav/div/span[2]'),
    ('<a>Top 12 Online Classifieds in Great Falls, Montana</a>', '/html/body/div/div[1]/section/section[4]/ul/li[5]/a'),
    ('<a>White Shorts</a>:', '/html/body/div/div[1]/section/section[5]/div/div/ul/li[5]/strong/a'),
    ('<p>Greensboro, located in the heart of North Carolina</p>', '/html/body/div/div[1]/div/main/div/article[4]/div/div/p'),
    ('<span class="menu-toggle-text">Menu</span>', '/html/body/div/header/div[2]/div/button/span'),
    ('<a>Craigslist Alternative Classifieds in Greensboro, </a>', '/html/body/div/div[1]/section/section[4]/ul/li[4]/a'),
    ('<a class="more-link">Continue reading</a>', '/html/body/div/div[1]/div/main/div/article[4]/div/div/a'),
    ('<a>Best Free Classifieds in Henderson, Nevada</a>', '/html/body/div/div[1]/section/section[4]/ul/li[3]/a'),
    ('<a class="more-link">Continue reading</a>', '/html/body/div/div[1]/div/main/div/article[1]/div/div/a'),
    ('<a>A Stylish Collection for Him: Unraveling Exquisite</a>', '/html/body/div/div[1]/section/section[4]/ul/li[1]/a'),
    ('<a class="url fn n">admin</a>', '/html/body/div/div[1]/div/main/div/article[3]/div/header/div/span[2]/span/a'),
    ('<a>White Skirts</a>:', '/html/body/div/div[1]/section/section[5]/div/div/ul/li[6]/strong/a'),
    ('<a>Shopping</a>', '/html/body/div/div[1]/div/main/div/article[4]/footer/div[1]/a[3]'),
    ('<a>White Tops</a>:', '/html/body/div/div[1]/section/section[5]/div/div/ul/li[8]/strong/a'),
    ('<a>Uncategorized</a>', '/html/body/div/div[1]/div/main/div/article[1]/footer/div[1]/a'),
    ('<a class="page-numbers">9</a>', '/html/body/div/div[1]/div/main/nav/div/a[3]'),
    ('<a>Pets</a>', '/html/body/div/header/div[2]/div/div/nav/ul/li[5]/a'),
    ('<a>Business</a>,', '/html/body/div/div[1]/div/main/div/article[4]/footer/div[1]/a[1]')
]

# Create a BeautifulSoup object
with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find the author names and their XPaths
authors = soup.find_all('a', class_='url fn n')
xpaths = [element[1] for element in html_elements]

# Create a list of scraped data
scraped_data = zip(authors, xpaths)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Author', 'XPath'])
    writer.writerows(scraped_data)