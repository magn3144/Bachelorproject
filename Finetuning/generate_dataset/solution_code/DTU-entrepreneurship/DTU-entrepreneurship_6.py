import csv
from lxml import etree

# Define XPaths for the 'Persons' label and its corresponding text
persons_xpath = '/html/body/form/div[3]/header/div[1]/div[2]/div/div[3]/div/div[2]/ul/li[2]/label'
persons_text_xpath = '/html/body/form/div[3]/header/div[1]/div[2]/div/div[3]/div/div[2]/ul/li[2]/label/text()'

def scrape_html():
    # Open the HTML file
    with open('downloaded_pages/DTU-entrepreneurship.html', 'r') as file:
        html = file.read()

    # Parse the HTML
    parser = etree.HTMLParser()
    tree = etree.parse(etree.HTML(html), parser)

    # Find the 'Persons' label element
    persons_label = tree.xpath(persons_xpath)[0]

    # Retrieve the text from the 'Persons' label
    persons_text = persons_label.xpath(persons_text_xpath)
  
    # Prepare the data to be saved as CSV
    header = ['Persons']
    data = [persons_text]

    # Save the data as CSV
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerow(data)


# Call the function to scrape HTML and save the data as CSV
scrape_html()