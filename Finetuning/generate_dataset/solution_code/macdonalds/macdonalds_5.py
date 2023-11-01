import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Define the XPath for the buttons
button_xpath = "//a[@class='button']"

# Set up Chrome driver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Specify the path to the Chrome driver executable
driver_path = "path_to_chrome_driver"

# Set up the Chrome driver
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Load the local HTML file
driver.get("file:///path_to_html_file")

# Find all the buttons using XPath
buttons = driver.find_elements(By.XPATH, button_xpath)

# Scrape the text from the buttons
button_texts = [button.text for button in buttons]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Button Text'])
    writer.writerows([[text] for text in button_texts])

# Quit the Chrome driver
driver.quit()