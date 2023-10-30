import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open the local HTML file
driver.get("file:///path/to/downloaded_pages/woman.html")

# Define the XPaths for the navigation links
navigation_xpaths = [
    '/html/body/div[6]/div[2]/header/div[2]/div/div[1]/nav/div[1]/ul/li[2]/ul/li[3]/a',
    '/html/body/div[6]/div[2]/header/div[2]/div/div[1]/nav/div[1]/ul/li[3]/ul/li[1]/a',
    '/html/body/div[6]/div[2]/header/div[2]/div/div[1]/nav/div[1]/ul/li[3]/ul/li[4]/a',
    '/html/body/div[6]/div[2]/header/div[2]/div/div[1]/nav/div[1]/ul/li[3]/ul/li[5]/a',
    '/html/body/div[6]/div[2]/header/div[2]/div/div[1]/nav/div[1]/ul/li[5]/ul/li[1]/a',
    '/html/body/div[6]/div[2]/header/div[2]/div/div[1]/nav/div[1]/ul/li[5]/ul/li[2]/a',
    '/html/body/div[6]/div[2]/header/div[2]/div/div[1]/nav/div[1]/ul/li[6]/ul/li[2]/a',
    '/html/body/div[6]/div[2]/header/div[2]/div/div[1]/nav/div[1]/ul/li[6]/ul/li[3]/a',
    '/html/body/div[6]/div[2]/header/div[2]/div/div[1]/nav/div[1]/ul/li[9]/ul/li[1]/a',
]

# Scrape the navigation link texts
navigation_texts = []
for xpath in navigation_xpaths:
    element = driver.find_element(By.XPATH, xpath)
    navigation_texts.append(element.text)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Navigation Links'])
    writer.writerows(zip(navigation_texts))
    
# Quit the browser
driver.quit()