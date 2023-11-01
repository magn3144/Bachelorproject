```
import csv
from lxml import etree

# Define the HTML elements and their corresponding XPaths
elements = [
    {
        'element': 'li',
        'xpath': '/html/body/footer/div[4]/div/div/div[2]/ul/li[1]'
    },
    {
        'element': 'h6',
        'xpath': '/html/body/header/div[3]/div[2]/div/div[3]/div[1]/h6'
    },
    {
        'element': 'li',
        'xpath': '/html/body/footer/div[4]/div/div/div[2]/ul/li[2]'
    },
    {
        'element': 'h6',
        'xpath': '/html/body/header/div[3]/div[2]/div/div[3]/div[2]/h6'
    },
    {
        'element': 'li',
        'xpath': '/html/body/footer/div[4]/div/div/div[2]/ul/li[3]'
    },
    {
        'element': 'h6',
        'xpath': '/html/body/header/div[3]/div[2]/div/div[3]/div[3]/h6'
    }
]

# Define the local path to the HTML file
local_path = 'downloaded_pages/coolshop.html'

def get_element_text(element, xpath):
    # Parse the HTML file
    parser = etree.HTMLParser()
    tree = etree.parse(local_path, parser)
    
    # Find the element using the XPath
    element = tree.xpath(xpath)[0]
    
    # Return the text of the element
    return element.text

def main():
    scraped_data = []
    
    # Iterate over the elements and scrape the data
    for elem in elements:
        text = get_element_text(elem['element'], elem['xpath'])
        scraped_data.append({
            'Title': elem['element'],
            'Link': elem['xpath'],
            'Text': text
        })
    
    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Link', 'Text'])
        writer.writeheader()
        writer.writerows(scraped_data)

if __name__ == '__main__':
    main()
```