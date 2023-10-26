import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Selenium webdriver
driver = webdriver.Chrome()
driver.get("file:///path/to/downloaded_pages/almanac.html")

# Scrape the extended forecast for a specific location
location = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[1]/h1").text
forecast = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/p[3]").text

# Save the scraped data as a CSV file
data = [[location, forecast]]
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Close the webdriver
driver.quit()