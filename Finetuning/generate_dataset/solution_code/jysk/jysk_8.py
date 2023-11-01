import csv
from lxml import etree

# Function to extract text from an element using XPath
def extract_text(element, xpath):
    extracted_text = element.xpath(xpath)
    if extracted_text:
        return extracted_text[0].strip()
    else:
        return ""

# Function to scrape the webpage and save the data as a CSV file
def scrape_webpage():
    # Read the HTML file
    with open('downloaded_pages/jysk.html', 'r') as file:
        html_content = file.read()

    # Parse the HTML content
    parser = etree.HTMLParser()
    tree = etree.fromstring(html_content, parser)

    # Initialize the scraped data list
    scraped_data = []

    # Extract text descriptions of different sections using the given XPaths
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[1]/div/div/div/div/div/a[4]/span/span'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[4]/div[2]/div/div/p[1]/a'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[1]/div/div/nav/ul/li[8]/a'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[1]/header/div/div/div/div[1]/div/a/svg/title'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[6]/div/div/div[4]/a/div/div[2]/div'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[2]/div/div/div[4]/a/div/div[2]/div'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[3]/section/div/div/div/p[1]'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[2]/div[1]/div/p'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[3]/section/div/div/div/form/div[4]/div/label'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[1]/div/div/div/div/div/a[2]/span/span'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[3]/section/div/div/div/form/div[1]/div/div/label/span/a[1]'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[3]/div[2]/div/nav/ul/li[9]/a'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[6]/div/div/div[2]/a/div/div[2]/div'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[2]/div/div/div[1]/a/div/div[2]/div'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[3]/section/div/div/div/p[2]'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[4]/div[1]/p'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[3]/section/div/div/div/form/div[2]/div/label'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/div/div/a[2]/span'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[5]/div/div[2]/div/div[1]/article/div[1]/h2/a'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[2]/div[2]/div/nav/ul/li[2]/a'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[6]/div/div/div[3]/a/div/div[2]/div'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[2]/div/div/div[2]/a/div/div[2]/div'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[5]/div/div[2]/div/div[1]/article/div[1]/div/p'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[4]/div/div/div[1]/p'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[3]/div/div/div[2]/div/div[4]/a/span[1]/span'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[2]/div[2]/div/nav/ul/li[4]/a'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[3]/div[2]/div/nav/ul/li[4]/a'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[2]/div/div/div[3]/a/div/div[2]/div'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[5]/div/div[2]/div/div[2]/article/div[1]/div/p'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[3]/div[1]/div/p'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[3]/div/div/div[2]/div/div[6]/a/span[1]/span'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[1]/div[2]/div/nav/ul/li[5]/a'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[6]/div/div/div[1]/a/div/div[2]/div'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[5]/div/div[1]/p'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/div/div/a[3]/span'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[4]/div[2]/div/div/p[2]/a[2]'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[1]/div/div/div/div[2]'))
    scraped_data.append(extract_text(tree, '/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[1]/div[1]/div/p'))

    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows([scraped_data])

# Call the function to scrape the webpage and save the data as a CSV file
scrape_webpage()