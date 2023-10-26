import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up the Chrome driver
service = Service('path/to/chromedriver') # Add the path to chromedriver
options = Options()
options.add_argument("--headless") # Run Chrome in headless mode
driver = webdriver.Chrome(service=service, options=options)

# Load the web page
driver.get("file:///path/to/downloaded_pages/century21.html") # Add the path to the downloaded HTML file

# Find the element using XPath
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/div/div[1]/div/fieldset/label/span")

# Get the text from the element
text = element.text

# Save the text as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([text])

# Quit the driver
driver.quit()