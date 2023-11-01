import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the path to the ChromeDriver executable
CHROMEDRIVER_PATH = 'path/to/chromedriver.exe'

# Define the local path to the HTML file
LOCAL_HTML_PATH = 'downloaded_pages/textures.html'

# Category of the page
CATEGORY = 'Digital Websites'

# The HTML elements and XPaths
elements = [
    {'element': 'texture_name', 'xpath': '//*[@id="texture-name"]'},
    {'element': 'download_link', 'xpath': '//*[@id="download-link"]'},
]

# Set up Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)

# Load the local HTML file
driver.get(f'file://{LOCAL_HTML_PATH}')

# Wait for the specific category to load
category_xpath = f"//a[contains(text(), '{CATEGORY}')]"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, category_xpath)))

# Find all the texture names and download links
results = []
for element in elements:
    element_name = element['element']
    element_xpath = element['xpath']
    elements = driver.find_elements(By.XPATH, element_xpath)
    values = [e.text for e in elements]
    results.append({element_name: values})

# Save the scraped data as a CSV file
fieldnames = ['texture_name', 'download_link']
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(results[0]['texture_name'])):
        row = {key: results[j][key][i] for j, key in enumerate(fieldnames)}
        writer.writerow(row)

# Quit the Chrome WebDriver
driver.quit()