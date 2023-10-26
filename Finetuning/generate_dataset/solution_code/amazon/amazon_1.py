import csv
from lxml import etree

def extract_department_categories(html_file):
    tree = etree.parse(html_file)
    root = tree.getroot()

    department_categories = []

    for element, xpath in html_elements:
        department_category = root.xpath(xpath)
        if department_category:
            department_categories.append(department_category[0].text)

    with open('scraped_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Department Categories'])
        writer.writerows(department_categories)

if __name__ == "__main__":
    html_file = "downloaded_pages/amazon.html"
    html_elements = [
        ("<label class='nav-progressive-attribute' id='searchDropdownDescription'>Select the department you want to search in</label>",
         "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/label"),
        ("<td> </td>", "/html/body/div[1]/div[3]/div[4]/table/tbody/tr[4]/td"),
        ("<td> </td>", "/html/body/div[1]/div[3]/div[4]/table/tbody/tr[2]/td"),
        ("<td> </td>", "/html/body/div[1]/div[3]/div[4]/table/tbody/tr[6]/td"),
        ("<td class='navFooterDescItem'> </td>", "/html/body/div[1]/div[3]/div[4]/table/tbody/tr[7]/td[13]"),
        ("<label>Search Amazon</label>", "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/label"),
        ("<div id='nav-progressive-subnav'></div>", "/html/body/div[1]/header/div/div[6]"),
        ("<a class='skip-link' id='skiplink'>Skip to main content</a>", "/html/body/div[1]/a[2]")
    ]

    extract_department_categories(html_file)