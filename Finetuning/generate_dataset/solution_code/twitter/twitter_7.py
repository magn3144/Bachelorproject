import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set the path to the ChromeDriver executable
chrome_driver_path = '/path/to/chromedriver'

# Set the options to run ChromeDriver in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Create a new ChromeDriver instance
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Load the HTML file from the local path
driver.get('file:///path/to/downloaded_pages/twitter.html')

# Find the desired element by XPath
element = driver.find_element(By.XPATH, '/html/body/noscript/div/p[3]/a[1]')

# Scrape the text from the element
scraped_text = element.text

# Close the ChromeDriver instance
driver.quit()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([scraped_text])
