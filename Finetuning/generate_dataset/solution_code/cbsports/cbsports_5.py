import csv
from selenium import webdriver

# Define the target url and local path to the HTML file
url = "https://cbsports.com"
local_path = "downloaded_pages/cbsports.html"

# Configure the webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(options=options)
driver.get(url)

# Save the HTML to a local file
with open(local_path, "w", encoding="utf-8") as file:
    file.write(driver.page_source)

# Function to fetch the text from all header tags
def fetch_header_text():
    with open(local_path, "r", encoding="utf-8") as file:
        html = file.read()
        driver.get("data:text/html;charset=utf-8," + html)
        
        header_tags = driver.find_elements_by_xpath("//h1 | //h2 | //h3 | //h4 | //h5 | //h6")
        header_texts = [tag.text.strip() for tag in header_tags]
        
        return header_texts

# Fetch the header text and save it as a CSV file
header_text = fetch_header_text()
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Header"])
    writer.writerows([[text] for text in header_text])

driver.quit()