import csv
from lxml import etree

# Set the path to the HTML file
html_path = 'downloaded_pages/wordpress.html'

# Define the XPaths for the HTML elements
xpaths = {
    'linkedin_account': '/html/body/div/footer/div/ul/li[4]/a/span'
}

def get_html_element(path, xpath):
    # Parse the HTML file
    with open(path, 'r') as file:
        html_content = file.read()
    html_tree = etree.HTML(html_content)
    
    # Find the HTML element using the XPath
    element = html_tree.xpath(xpath)
    return element[0].text if element else ''

def save_as_csv(data):
    # Define the CSV file name
    file_name = 'scraped_data.csv'
    
    # Write the data to the CSV file
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['LinkedIn Account'])
        writer.writerow([data])

def main():
    # Get the LinkedIn account text
    linkedin_account = get_html_element(html_path, xpaths['linkedin_account'])
    
    # Save the LinkedIn account text as a CSV file
    save_as_csv(linkedin_account)

if __name__ == '__main__':
    main()