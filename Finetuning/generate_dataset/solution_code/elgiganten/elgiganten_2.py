import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set Chrome options to run the browser in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Load the local HTML file
driver.get('file:///path/to/downloaded_pages/elgiganten.html')

# Find the "Kundeservice" hyperlink
link_element = driver.find_element(By.XPATH, '/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/div[2]/elk-navigation/div/mat-expansion-panel[1]/div/div/div/ul/li[1]/a')

# Extract the link and text
link = link_element.get_attribute('href')
text = link_element.text

# Store the data in a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Link', 'Text'])
    writer.writerow([link, text])

# Quit the browser
driver.quit()