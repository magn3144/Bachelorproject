import csv
from selenium import webdriver

# Set up the Selenium web driver
driver = webdriver.Chrome()

# Load the local HTML file
driver.get("file:///downloaded_pages/quora.html")

# Find all the user names
user_elements = driver.find_elements_by_xpath("//div[@class='User']//a[@class='UserCredential']")

# Find all the answer elements
answer_elements = driver.find_elements_by_xpath("//div[@class='Answer']//p")

# Create a list to store the scraped data
scraped_data = []

# Extract the user names and associated answers
for i in range(len(user_elements)):
    user_name = user_elements[i].text
    answer = answer_elements[i].text
    scraped_data.append([user_name, answer])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(scraped_data)

# Close the web driver
driver.quit()