import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/trustpilot.html', 'r') as file:
    html = file.read()
    
# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Initialize the scraped data list
scraped_data = []

# Define the XPaths and corresponding element text
xpaths = [
    ("/html/body/div/div/div/main/div/div[2]/div/div[1]/ul/li[6]/a/span", "Erhvervsforsikringsselskab"),
    ("/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[6]/a/div[2]/span", "Rejseforsikringsselskab"),
    ("/html/body/div/div/div/footer/div/div/div[2]/ul/li[4]/a", "Retningslinjer for brugere"),
    ("/html/body/div/div/div/footer/div/div/section[2]/ul/li[7]/a", "Presse"),
    ("/html/body/div/div/div/main/div/div[2]/div/div[3]/div/div/div[8]/a/p", "BUPA DENMARK, FILIAL AF BUPA INSURANCE LIMITED, EN"),
    ("/html/body/div/div/div/main/div/div[2]/aside/div[2]/ul/li[2]/a/p", "1"),
    ("/html/body/div/div/div/main/div/div[2]/aside/div[1]/fieldset[1]/legend", "Sortér efter"),
    ("/html/body/div/div/div/footer/div/div/div[2]/div", "© 2023 Trustpilot A/S. Alle rettigheder forbeholde"),
    ("/html/body/div/div/div/main/div/div[2]/div/section/div[5]/a/div[1]", "Mest relevant"),
    ("/html/body/div/div/div/main/div/div[2]/div/div[2]/h2", "Nyligt anmeldte virksomheder"),
    ("/html/body/div/div/div/footer/div/div/section[1]/h3", "Vælg land"),
    ("/html/body/div/div/div/main/div/div[2]/aside/div[2]/ul/li[6]/a/span", "Erhvervsforsikringsselskab"),
    ("/html/body/div/div/div/main/div/div[2]/div/div[3]/div/div/div[1]/a/div[2]/span", "Rejseforsikringsselskab"),
    ("/html/body/div/div/div/footer/div/div/div[2]/ul/li[3]/a", "Vilkår og betingelser"),
    ("/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[4]/a/div[3]/div/div/p[2]", "Hurtig og rigtig god service."),
    ("/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[6]/a/div[3]/div/div/p[2]", "God rådgivning!"),
    ("/html/body/div/div/div/main/div/div[2]/aside/div[1]/fieldset[2]/legend", "Lokation"),
    ("/html/body/div/div/div/main/div/div[2]/div/section/div[4]/a/div[1]", "Mest relevant"),
    ("/html/body/div/div/div/main/div/div[2]/div/div[3]/h2", "Nye virksomheder på Trustpilot"),
    ("/html/body/div/div/div/footer/div/div/section[2]/h3", "Om os"),
    ("/html/body/div/div/div/main/div/div[2]/div/div[1]/ul/li[2]/a/span", "Begravelsesforsikringsselskab"),
    ("/html/body/div/div/div/footer/div/div/section[1]/div/dl/div/dd/ul/li[9]/button/span[2]", "New Zealand"),
    ("/html/body/div/div/div/footer/div/div/section[4]/ul/li[1]/a", "Trustpilot Business"),
    ("/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[7]/a/div[3]/div/div/p[2]", "Gennemsnitlig oplevelse. Helt ok."),
    ("/html/body/div/div/div/main/div/div[2]/div/div[1]/ul/li[4]/a/p", "4"),
    ("/html/body/div/div/div/main/div/div[2]/aside/div[1]/fieldset[3]/legend", "Virksomhedsstatus"),
    ("/html/body/div/div/div/footer/div/div/section[5]/h3", "Følg os på"),
    ("/html/body/div/div/div/main/div/div[2]/aside/div[2]/ul/li[2]/a/span", "Begravelsesforsikringsselskab"),
    ("/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[4]/a/div[2]/span[1]", "Forsikringsvirksomhed"),
    ("/html/body/div/div/div/footer/div/div/section[3]/ul/li[2]/a", "Supportcenter"),
    ("/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[8]/a/div[3]/div/div/p[2]", "Brilliant service og pris.Jeg valgte SafeAway da")
]

# Scrape the data using the XPaths
for xpath, text in xpaths:
    element = soup.find(xpath=xpath)
    if element:
        scraped_data.append((text, element.text))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(scraped_data)