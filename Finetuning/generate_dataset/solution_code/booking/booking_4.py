import csv
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the ChromeDriver executable
CHROME_DRIVER_PATH = "path/to/chromedriver"

# Set the local path to the HTML file
HTML_FILE_PATH = "downloaded_pages/booking.html"

# Set the category
CATEGORY = "Tourism"

# Set the output CSV file name
OUTPUT_FILE = "scraped_data.csv"

# Create a ChromeDriver service
driver_service = Service(CHROME_DRIVER_PATH)

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

# Create a new ChromeDriver instance
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

# Load the local HTML file
driver.get("file://" + os.getcwd() + "/" + HTML_FILE_PATH)

# Wait for the page to fully load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='a53cbfa6de e7c28a2436']")))

# Find and extract the address and contact information of each property
properties = driver.find_elements(By.XPATH, "//div[@class='a53cbfa6de e7c28a2436']")
data = []
for prop in properties:
    address = prop.text
    contact_info = prop.get_attribute("innerHTML")
    data.append((address, contact_info))

# Close the ChromeDriver instance
driver.quit()

# Save the extracted data as a CSV file
with open(OUTPUT_FILE, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Address', 'Contact Info'])
    writer.writerows(data)