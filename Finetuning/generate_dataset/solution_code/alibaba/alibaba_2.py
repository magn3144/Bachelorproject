import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Chrome driver
driver = webdriver.Chrome('/path/to/chromedriver')

# Load the web page
driver.get('file:///path/to/downloaded_pages/alibaba.html')

# Find the personal protective equipment span element
ppe_element = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div[1]/div/div[1]/ul/li[6]/div/a/span')

# Get the text content of the personal protective equipment span
ppe_text = ppe_element.text

# Save the scraped data as CSV
with open('scraped_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([ppe_text])

# Close the browser
driver.quit()