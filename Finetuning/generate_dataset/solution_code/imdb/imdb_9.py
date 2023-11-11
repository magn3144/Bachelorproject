import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the web driver
driver = webdriver.Chrome()

# Open the local HTML file
driver.get("file:///path/to/downloaded_pages/imdb.html")

# Find all the movie titles and release years
titles = driver.find_elements(By.XPATH, "//h3[@class='ipc-title__text']")
release_years = driver.find_elements(By.XPATH, "//span[@class='sc-c7e5f54-8 fiTXuB cli-title-metadata-item']")

# Create a list to store the scraped data
scraped_data = []
for title, release_year in zip(titles, release_years):
    scraped_data.append({"Title": title.text, "Release Year": release_year.text})

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Release Year"])
    writer.writeheader()
    writer.writerows(scraped_data)

# Close the web driver
driver.quit()