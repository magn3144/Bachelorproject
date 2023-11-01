import csv
from urllib.request import urlopen
from lxml import etree


def get_html_element_text(html_path):
    try:
        with open(html_path, 'r') as file:
            return file.read()
    except IOError:
        print(f"Error: Could not open file '{html_path}'")


def extract_data(html, xpath):
    try:
        tree = etree.HTML(html)
        elements = tree.xpath(xpath)
        return [element.text.strip() for element in elements]
    except Exception as e:
        print(f"Error: Failed to extract data with XPath '{xpath}': {e}")


def save_data_as_csv(data):
    try:
        with open('scraped_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("Data saved successfully as 'scraped_data.csv'")
    except Exception as e:
        print(f"Error: Failed to save data as CSV: {e}")


def main():
    html_path = 'downloaded_pages/google.html'
    xpath = '/html/body/div[2]/div/ul/li[2]/div/div/p[3]'
    html = get_html_element_text(html_path)
    data = extract_data(html, xpath)
    save_data_as_csv([data])


if __name__ == "__main__":
    main()
