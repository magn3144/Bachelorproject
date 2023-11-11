import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize ChromeDriver
driver = webdriver.Chrome()

# Load the local HTML file
driver.get("file:///path/to/downloaded_pages/DTU-entrepreneurship.html")

# Find the "News and events" button by XPath
button = driver.find_element(By.XPATH, "/html/body/form/div[3]/header/div[2]/div/div/nav/ul/li[6]/div/div/a")

# Get the text from the button
button_text = button.text

# Save the button text as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["News and events"])
    writer.writerow([button_text])

# Close the driver
driver.quit()