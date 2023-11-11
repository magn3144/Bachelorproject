import csv
from lxml import etree

# Define the HTML file path
html_file_path = "downloaded_pages/airbnb.html"

# Define the XPaths for the elements in the Site Footer
site_footer_heading_xpath = "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/span/h2"
site_footer_section_1_xpath = "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[1]/ul"
site_footer_section_2_xpath = "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[2]/ul"
site_footer_section_3_xpath = "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/ul"

# Parse the HTML file
tree = etree.parse(html_file_path)

# Find the site footer heading
site_footer_heading_element = tree.xpath(site_footer_heading_xpath)[0]
site_footer_heading_text = site_footer_heading_element.text

# Find the elements in section 1 of the site footer
section_1_elements = tree.xpath(site_footer_section_1_xpath + "/li/a")
section_1_data = [element.text for element in section_1_elements]

# Find the elements in section 2 of the site footer
section_2_elements = tree.xpath(site_footer_section_2_xpath + "/li/a")
section_2_data = [element.text for element in section_2_elements]

# Find the elements in section 3 of the site footer
section_3_elements = tree.xpath(site_footer_section_3_xpath + "/li/a")
section_3_data = [element.text for element in section_3_elements]

# Create a CSV file and write the data
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Site Footer Heading', 'Section 1', 'Section 2', 'Section 3'])
    writer.writerow([site_footer_heading_text, ','.join(section_1_data),
                     ','.join(section_2_data), ','.join(section_3_data)])