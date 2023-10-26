import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Set up the ChromeDriver and Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
selenium_service = Service('/path/to/chromedriver')

# Start the WebDriver
driver = webdriver.Chrome(service=selenium_service, options=chrome_options)

# Load the HTML file
driver.get('file:///path/to/downloaded_pages/edx.html')

# Find the "Executive Education" heading
heading_xpath = '/html/body/div[1]/div[1]/div/main/div/div[8]/div[1]/div/div/div/div/div[1]/a/h3'
heading_element = driver.find_element(By.XPATH, heading_xpath)
heading_text = heading_element.text

# Save the scraped data as a CSV file
data = [{'Heading': heading_text}]

with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Heading'])
    writer.writeheader()
    writer.writerows(data)

# Quit the WebDriver
driver.quit()