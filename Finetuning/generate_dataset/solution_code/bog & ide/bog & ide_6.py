import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Set up Chrome Options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


# Set up Chrome Driver Service
service = Service('/path/to/chromedriver')


# Choose Chrome Browser
driver = webdriver.Chrome(service=service, options=chrome_options)


# Load the web page
driver.get('file:///path/to/downloaded_pages/bog%20&%20ide.html')


# Find the element with the class "css-1njy7qn-ImageTextSpotText"
element = driver.find_element(By.CLASS_NAME, "css-1njy7qn-ImageTextSpotText")


# Get the text from the element
text = element.text


# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([text])


# Quit the driver
driver.quit()