import csv
import lxml.html as lh

file_path = "downloaded_pages/DTU_entrepreneurship.html"

# Load webpage
with open(file_path, "r") as f:
    page_content = f.read()

# Parse content
tree = lh.fromstring(page_content)

# Extract address
address_xpath = '/html/body/form/div[3]/footer/div[1]/div/div[2]/div[2]/div[1]'
address_element = tree.xpath(address_xpath)
address_value = address_element[0].text_content().strip().replace('"', '')

# Add quotation marks around the whole address
formatted_address = '"' + address_value + '"'

# Save to csv file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([formatted_address])