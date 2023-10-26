import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to the ChromeDriver executable
chrome_driver_path = '/path/to/chromedriver'

# Set the path to the downloaded HTML file
html_file_path = 'downloaded_pages/alibaba.html'

# Set the category
category = 'E-commerce'

# Set the XPaths for the target elements
div_xpath = '/html/body/div[1]/header/div[2]/div[4]/div[1]/div[2]/div/div[1]/div'

# Set the task
task = 'Get the text content of the sc-hd-ms-info div and save it as a CSV file.'

# Set the output file name
output_file = 'scraped_data.csv'

# Set up the ChromeDriver options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode

# Start the ChromeDriver service
s = Service(chrome_driver_path)
s.start()

# Start the Chrome browser
driver = webdriver.Chrome(service=s, options=chrome_options)

# Load the HTML file
driver.get('file://' + html_file_path)

# Find the target div element
div_element = driver.find_element(By.XPATH, div_xpath)

# Get the text content of the div element
text_content = div_element.text.strip()

# Save the data as a CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category', 'Task', 'Result'])
    writer.writerow([category, task, text_content])

# Quit the browser and stop the ChromeDriver service
driver.quit()
s.stop()