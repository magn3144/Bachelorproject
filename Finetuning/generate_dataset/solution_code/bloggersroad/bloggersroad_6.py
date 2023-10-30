import csv
from selenium import webdriver

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Load the local HTML file
driver.get("file:///path/to/downloaded_pages/bloggersroad.html")

# Retrieve the search bar label and its XPath
search_bar_label_xpath = '/html/body/div/div[1]/section/section[3]/form/label/span'
search_bar_label = driver.find_element_by_xpath(search_bar_label_xpath).text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Search Bar Label', 'XPath'])
    writer.writerow([search_bar_label, search_bar_label_xpath])

# Close the WebDriver
driver.quit()