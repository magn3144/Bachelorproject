from bs4 import BeautifulSoup
import csv

html_path = "downloaded_pages/merchantcircle.html"
category = "Directories"
elements = [
    {
        "element": '<a>Cryptocurrency Evolution: Navigating the Intersect</a>',
        "xpath": '/html/body/div[1]/div[4]/section/section[4]/section[3]/h2/a'
    },
    {
        "element": '<a>...</a>',
        "xpath": '/html/body/div[1]/div[4]/main/div/a[6]'
    },
    {
        "element": '<a>About Us</a>',
        "xpath": '/html/body/footer/div/div/ul/li[2]/ul/li[1]/a'
    },
    {
        "element": '<a>Read More…</a>',
        "xpath": '/html/body/div[1]/div[4]/main/section/section[4]/div/div[1]/div[2]/span/a'
    },
    {
        "element": '<a>FREE MOVING ESTIMATE www.movers-newyorkcity.com</a>',
        "xpath": '/html/body/div[1]/div[4]/section/section[3]/section[2]/div/div/h2/a'
    },
    {
        "element": '<a class="btn-filled">Website</a>',
        "xpath": '/html/body/div[1]/div[4]/main/section/section[8]/div/div[2]/div/a[2]'
    },
    {
        "element": '<a> Buy phentermine Without Perscription</a>',
        "xpath": '/html/body/div[1]/div[4]/section/section[4]/section[1]/h2/a'
    },
    {
        "element": '<a class="viewMoreLink">...read more</a>',
        "xpath": '/html/body/div[1]/div[4]/section/section[1]/section[1]/div[2]/p/a'
    },
    {
        "element": '<a>Expert Insights</a>',
        "xpath": '/html/body/footer/div/div/ul/li[4]/ul/li[2]/a'
    },
    {
        "element": '<a>Terms of Use</a>',
        "xpath": '/html/body/footer/div/div/ul/li[2]/ul/li[2]/a'
    }
]

# Extract names and URLs
data = []
for element in elements:
    soup = BeautifulSoup(element['element'], 'html.parser')
    name = soup.a.text
    url = soup.a['href']
    data.append({'Name': name, 'URL': url})

# Save data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'URL']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)