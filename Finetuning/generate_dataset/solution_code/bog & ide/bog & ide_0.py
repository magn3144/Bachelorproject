import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Chrome driver
driver = webdriver.Chrome()

# Load the local HTML file
driver.get("file:///path/to/downloaded_pages/bog%20%26%20ide.html")

# Create a list to store scraped data
data = []

# Scrape the elements using their XPaths
element_1 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[2]/div[2]/div/div/div/div[8]/div/div/span[2]").text
element_2 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[4]/div[2]/div/div/div/div[12]/div/a/span").text
element_3 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div/h2/a").text
element_4 = driver.find_element(By.XPATH, "/html/body/div/header/ul/li[1]/ul/li[10]/ul/li[5]/a").text
element_5 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[1]/div[2]/div/div/div/a[1]/div").text
element_6 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[2]/div[2]/div/div/p").text
element_7 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[1]/div[1]/h2").text
element_8 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[4]/div[1]/h2").text
element_9 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[4]/div/div[1]/h4").text
element_10 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[3]/div/div[1]/h4").text
element_11 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[7]/div[2]/div/div/div/div[14]/div/div/span[1]").text
element_12 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[1]/div[2]/div/div/div/div[10]/div/div/span[2]").text
element_13 = driver.find_element(By.XPATH, "/html/body/div/header/ul/li[1]/ul/li[6]/ul/li[11]/a").text
element_14 = driver.find_element(By.XPATH, "/html/body/div/header/ul/li[2]/ul/li[20]/ul/li[5]/a").text
element_15 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[6]/div[2]/div/div/div/a[1]/div").text
element_16 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/p").text
element_17 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[2]/div[1]/h2").text
element_18 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[5]/div[1]/h2").text
element_19 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[1]/div[2]/div/div/div/div[11]/div/div/span[1]").text
element_20 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[3]/div[2]/div/div/div/div[5]/div/div/span[2]").text
element_21 = driver.find_element(By.XPATH, "/html/body/div/header/ul/li[6]/ul/li[7]/ul/li[2]/a").text
element_22 = driver.find_element(By.XPATH, "/html/body/div/header/ul/li[6]/ul/li[11]/ul/li[2]/a").text
element_23 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/div/a[1]/div").text
element_24 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[6]/div[2]/div/div/p").text
element_25 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[3]/div[1]/h2").text
element_26 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[6]/div[1]/h2").text
element_27 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[4]/div[2]/div/div/div/div[6]/div/a/span").text
element_28 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/section[2]/div[2]/div/div/div/div[6]/div/div/span[2]").text
element_29 = driver.find_element(By.XPATH, "/html/body/div/header/ul/li[6]/ul/li[5]/ul/li[9]/a").text
element_30 = driver.find_element(By.XPATH, "/html/body/div/header/ul/li[1]/ul/li[3]/ul/li[4]/a").text
element_31 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div/div/a[1]/div").text
element_32 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[6]/div[2]/div/div/div/a[1]/div").text
element_33 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/div/a[1]/div").text
element_34 = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[6]/div[2]/div/div/div/a[1]/div").text

# Append the scraped data to the list
data.append([element_1, element_2, element_3, element_4, element_5, element_6, element_7, element_8, element_9, element_10, element_11, element_12, element_13, element_14, element_15, element_16, element_17, element_18, element_19, element_20, element_21, element_22, element_23, element_24, element_25, element_26, element_27, element_28, element_29, element_30, element_31, element_32, element_33, element_34])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Close the driver
driver.quit()