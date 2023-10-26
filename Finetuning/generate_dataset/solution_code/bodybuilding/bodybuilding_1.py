import csv
from lxml import html

# Define the xpath for the FAQ questions
faq_question_xpaths = [
    '/html/body/section/main/div[7]/h2',
    '/html/body/section/main/div[7]/ul/li/div/div/ul/li',
]

# Create a list to store the scraped data
scraped_data = []

# Parse the HTML file
with open('downloaded_pages/bodybuilding.html', 'rb') as file:
    page_content = file.read()
    tree = html.fromstring(page_content)

    # Scrape the FAQ questions
    for xpath in faq_question_xpaths:
        faq_questions = tree.xpath(xpath)

        # Extract the question text and its corresponding XPath
        for question in faq_questions:
            question_text = question.text.strip()
            question_xpath = tree.getpath(question)

            # Append the data to the list
            scraped_data.append([question_text, question_xpath])

# Save the scraped data in a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Question', 'XPath'])
    writer.writerows(scraped_data)