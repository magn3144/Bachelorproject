import csv
from bs4 import BeautifulSoup

with open("downloaded_pages/DTU_entrepreneurship.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

text = soup.xpath("/html/body/form/div[3]/footer/div[1]/div/div[2]/h2").text

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Header", "Description"])
    writer.writerow(["CENTRE FOR TECHNOLOGY ENTREPRENEURSHIP", text])