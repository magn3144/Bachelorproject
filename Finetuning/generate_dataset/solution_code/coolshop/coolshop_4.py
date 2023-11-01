import csv
from lxml import etree

def collect_popular_products():
    # Open the HTML file
    with open('downloaded_pages/coolshop.html', 'r') as file:
        html = file.read()

    # Create an HTML tree from the HTML string
    tree = etree.HTML(html)

    # Find all elements with the class 'cpn-product-list-item'
    product_elements = tree.xpath('//div[contains(@class, "cpn-product-list-item")]')

    # Create a list to store the scraped data
    scraped_data = []

    # Iterate over each product element
    for element in product_elements:
        # Find the name of the product by getting the text of the child 'a' element
        name = element.xpath('.//a')[0].text

        # Find the link to the product by getting the value of the 'href' attribute of the child 'a' element
        link = element.xpath('.//a/@href')[0]

        # Append the name and link as a tuple to the scraped data list
        scraped_data.append((name, link))

    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Link'])
        writer.writerows(scraped_data)

# Call the function to collect and save the popular products
collect_popular_products()