import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set Chrome options to run the browser in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless") 

# Specify the path to the chromedriver executable
driver = webdriver.Chrome('path/to/chromedriver', options=chrome_options)

# Load the local HTML file
driver.get("file:///path/to/downloaded_pages/quora.html")

# Find all the user names and their associated comments
user_names = driver.find_elements(By.XPATH, "//div[@class='comment-user-name']")
comments = driver.find_elements(By.XPATH, "//div[@class='comment-text']")

# Create a list to store the scraped data
scraped_data = []
for i in range(len(user_names)):
    user_name = user_names[i].text
    comment = comments[i].text
    scraped_data.append([user_name, comment])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['User Name', 'Comment'])
    writer.writerows(scraped_data)

# Close the webdriver
driver.quit()