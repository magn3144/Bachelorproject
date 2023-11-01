import csv
from bs4 import BeautifulSoup

# Define the function to extract menu category data
def extract_menu_category_data(html_content, category_xpath):
    soup = BeautifulSoup(html_content, 'html.parser')
    category_elements = soup.select(category_xpath)
    data = []
    
    for element in category_elements:
        name = element.get_text(strip=True)
        xpath = element.get('xpath')
        data.append({'Name': name, 'XPath': xpath})
    
    return data

# Define the main function
def main():
    # Define the local path to the HTML file
    html_path = 'downloaded_pages/macdonalds.html'
    
    # Define the target category XPath
    category_xpath = '/html/body/div/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/nav/ul[2]/li[8]/a/span'
    
    # Read the HTML file
    with open(html_path, 'r') as f:
        html_content = f.read()
    
    # Extract the menu category data
    menu_category_data = extract_menu_category_data(html_content, category_xpath)
    
    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'XPath'])
        writer.writeheader()
        writer.writerows(menu_category_data)

# Execute the main function
if __name__ == '__main__':
    main()