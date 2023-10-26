import csv
from lxml import html

def scrape_text_content():
    # Define the XPaths for the span element
    xpaths = [
        '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[1]/div/div/div[2]/ul/li[2]/button/span[2]',
        '/html/body/div[2]/div/div/main/div[2]/div/div/div/div/div[2]/div[3]/div[2]/div[8]/a/span[1]',
        '/html/body/div[2]/div/div/main/div[2]/div/div/div/div/div[2]/ul/li[4]/div/div/div/div/div/div[2]/div[3]/div[4]/p',
        '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[5]/div/section/div/div[2]/div[1]/div[2]/div/p',
        '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[5]/div/section/div/div[2]/div[1]/div[1]/div/ul/li[2]/div/a/div/div/div[2]',
        '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[10]/div/section/div/div[2]/div[1]/div/div/ul/li[1]/div/a/div/div/div[2]',
        '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[14]/div/section/div/div[2]/div[2]/div[1]/ul/li[3]/div/a',
        '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[14]/div/section/div/div[2]/div[2]/div[2]/ul/li[1]/div/a',
        '/html/body/div[2]/div/div/div/footer/div/div/div/div[9]/div/div[1]/span',
        '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[12]/div/section/div/div[2]/div[1]/div[2]/div/ul/li[2]/div/a/div/div/div[2]/span/span',
        '/html/body/div[2]/div/div/main/div[2]/div/div/div/div/div[2]/ul/li[1]/div/div/div/div/div/div[2]/div[3]/div[3]/p',
        '/html/body/div[2]/div/div/main/div[1]/div/div/section/div/div[1]/div/div/div[9]/div/div/div/a/div/div[2]/p',
        '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[6]/div/section/div/div[2]/div[1]/div[1]/div/ul/li[4]/div/a/div/div/div[2]',
        '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[8]/div/section/div/div[2]/div[1]/div[1]/div/ul/li[6]/div/a/div/div/div[1]',
        '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[2]/div/section/div/div[2]/div[5]/ul/li[2]/a',
        '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[5]/div/section/div/div[2]/div[1]/div[1]/div/ul/li[7]/a',
        '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[6]/div/section/div/button/span/svg/title',
        '/html/body/div[2]/div/div/main/div[2]/div/div/div/div/div[2]/div[3]/div[1]/h2',
        '/html/body/div[2]/div/div/main/div[1]/div/div/section/div/div[1]/div/div/div[9]/div/div/div/a/div/div[2]/h3',
        '/html/body/div[2]/div/div/main/div[2]/div/div/div/div/div[2]/ul/li[4]/div/div/div/div/div/div[2]/div[1]/div[2]/a/h3'
    ]
    
    # Load the local HTML file
    with open('downloaded_pages/coursera.html', 'r') as file:
        content = file.read()
    
    # Parse the HTML content
    tree = html.fromstring(content)
    
    # Retrieve the text content from the span elements using XPaths
    span_text_content = []
    for xpath in xpaths:
        elements = tree.xpath(xpath)
        if elements:
            span_text_content.append(elements[0].text_content())
        else:
            span_text_content.append('')
    
    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Span Text Content'])
        writer.writerow(span_text_content)

scrape_text_content()