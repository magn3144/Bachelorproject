import csv
import lxml.html as lh
from selenium import webdriver

def scrape_data():
    path = "downloaded_pages/imdb.html"
    driver = webdriver.Firefox()
    driver.get("file:///" + path)

    movies = {}
    for i in range(1, 251):
        movie_title_xpath = f"/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/div[1]/a/h3"
        movie_meta_xpath = f"/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/div[2]/span[3]"
        title = driver.find_element_by_xpath(movie_title_xpath).text
        meta = driver.find_element_by_xpath(movie_meta_xpath).text
        movies[title] = meta

    with open('scraped_data.csv', 'w') as f:
        writer = csv.writer(f)
        for key, value in movies.items():
            writer.writerow([key, value])

    driver.close()

scrape_data()