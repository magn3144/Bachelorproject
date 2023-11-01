import csv
from lxml import html

# Function to extract question titles and upvotes
def extract_question_data(html_content):
    tree = html.fromstring(html_content)
    question_title_elements = tree.xpath('//div[@class="q-box qu-mb--tiny"]/div[@class="q-box qu-mb--tiny"]/div//span[@class="qlink_container"]/span/span[@class="q-box qu-align--center-space-between"]/span/a/span/span/span')
    upvote_elements = tree.xpath('//div[@class="q-box qu-mb--tiny"]/div[@class="q-box qu-mb--tiny"]/div//span[@class="qlink_container"]/span/span/span/span[@class="answer_count pull"]')
    
    scraped_data = []
    for title_element, upvote_element in zip(question_title_elements, upvote_elements):
        title = title_element.text.strip()
        upvotes = upvote_element.text.strip().split()[0]
        scraped_data.append([title, upvotes])
    
    return scraped_data

# Read the local HTML file
with open('downloaded_pages/quora.html') as file:
    html_content = file.read()

# Extract question data from HTML
question_data = extract_question_data(html_content)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Question Title', 'Upvotes'])
    writer.writerows(question_data)