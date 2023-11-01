import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set the path to the ChromeDriver executable
chrome_driver_path = 'path_to_chromedriver'

# Set the URL of the local HTML file
local_html_file_path = 'downloaded_pages/quora.html'

# Open the local HTML file in Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(f'file://{local_html_file_path}')

# Find all review ratings and comments using the provided XPath
review_ratings = driver.find_elements(By.XPATH, '//span[contains(@class, "review-rating")]')
review_comments = driver.find_elements(By.XPATH, '//div[contains(@class, "review-comment")]')

# Create a list to store the scraped data
scraped_data = []

# Iterate over each review rating and comment and extract the text
for rating, comment in zip(review_ratings, review_comments):
    rating_text = rating.text
    comment_text = comment.text
    scraped_data.append([rating_text, comment_text])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Rating', 'Comment'])
    writer.writerows(scraped_data)

# Close the Chrome WebDriver
driver.quit()