import csv
import requests
from lxml import html

def extract_course_description():
    with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as file:
        page_content = file.read()

    tree = html.fromstring(page_content)
    
    # Get the descriptions of the courses with the xpath //*[@id="outercontent"]/div[n]/div/div[1]/ul/li/a/text()
    # and store them in a list called descriptions
    div_count = len(tree.xpath('//*[@id="outercontent"]/div'))
    descriptions = []
    for n in range(1, div_count+1):
        for m in range(1, div_count+1):
            descriptions.append(tree.xpath(f'//*[@id="outercontent"]/div[{n}]/div/div[{m}]/ul/li/a/text()'))

    # Concatenate the descriptions into a single string
    descriptions = [' '.join(description) for description in descriptions]

    # Remove [, ], and ' from the descriptions
    descriptions = [description.replace('[', '').replace(']', '').replace("'", '') for description in descriptions]

    # Remove empty strings from the list
    descriptions = [description for description in descriptions if description != '']

    # Save the descriptions in a CSV file
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in descriptions:
            writer.writerow([row])

extract_course_description()