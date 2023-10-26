import csv
from lxml import etree

def get_text(element):
    if element is not None:
        return element.text.strip()
    return ""

def scrape_page():
    scraped_data = []
    with open("downloaded_pages/almanac.html", "r", encoding="utf-8") as file:
        html = file.read()
    tree = etree.HTML(html)
    
    # Scrape data
    data_1 = get_text(tree.xpath("/html/body/div[1]/div/div/footer/div/div[1]/div/nav[1]/ul/li[1]/a")[0])
    data_2 = get_text(tree.xpath("/html/body/div[1]/div/div/footer/div/div[1]/div/nav[2]/ul/li[5]/a")[0])
    data_3 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/div[2]/div")[0])
    data_4 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/table[2]/tbody/tr[1]/td/span/span")[0])
    data_5 = get_text(tree.xpath("/html/body/div[1]/div/div/header/div/div[2]/div/div[4]/nav/ul/li[1]/ul/li[1]/a/span")[0])
    data_6 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/h2[1]")[0])
    data_7 = get_text(tree.xpath("/html/body/div[1]/div/div/div[2]/div/nav/h2")[0])
    data_8 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/div[1]/div/form/div/div/label")[0])
    data_9 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[1]/h1")[0])
    data_10 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/table[1]/caption")[0])
    data_11 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/table[1]/tfoot/tr/th")[0])
    data_12 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[2]/div[2]/div/div/div/div[3]/a/p[1]")[0])
    data_13 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[2]/div[2]/div/div/div/div[4]/a/p[2]")[0])
    data_14 = get_text(tree.xpath("/html/body/div[1]/div/div/div[2]/div/nav/ul/li[1]/a")[0])
    data_15 = get_text(tree.xpath("/html/body/div[1]/div/div/div[2]/div/nav/ul/li[3]/a")[0])
    data_16 = get_text(tree.xpath("/html/body/div[3]")[0])
    data_17 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/table[1]/tbody/tr[3]/td/span/span")[0])
    data_18 = get_text(tree.xpath("/html/body/div[1]/div/div/header/div/div[2]/div/div[4]/div[2]/nav[2]/div/div/a[4]/span[2]")[0])
    data_19 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/h2[3]")[0])
    data_20 = get_text(tree.xpath("/html/body/div[1]/div/div/footer/div/div[2]/div/h2")[0])
    data_21 = get_text(tree.xpath("/html/body/div[1]/div/div/header/div/div[2]/div/div[4]/div[2]/nav[1]/form/div[1]/label")[0])
    data_22 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/table[2]/thead/tr/th[2]")[0])
    data_23 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/p[1]"))
    data_24 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[2]/div[2]/div/div/div/div[3]/a/p[3]")[0])
    data_25 = get_text(tree.xpath("/html/body/a")[0])
    data_26 = get_text(tree.xpath("/html/body/div[1]/div/div/footer/div/div[1]/div/nav[2]/ul/li[3]/a")[0])
    data_27 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/div")[0])
    data_28 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/table[1]/tbody/tr[2]/td/span/span")[0])
    data_29 = get_text(tree.xpath("/html/body/div[1]/div/div/header/div/div[2]/div/div[4]/nav/ul/li[2]/ul/li[8]/a/span")[0])
    data_30 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[1]/div[2]/h2")[0])
    data_31 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[2]/div/div/nav/h2")[0])
    data_32 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[1]/div[2]/div/form/div/label")[0])
    data_33 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/table[2]/tfoot/tr/th")[0])
    data_34 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/p[3]"))
    data_35 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[2]/div[2]/div/div/div/div[1]/a/p[2]")[0])
    data_36 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/p[2]/a")[0])
    data_37 = get_text(tree.xpath("/html/body/div[1]/div/div/footer/div/div[1]/div/nav[1]/ul/li[2]/a")[0])
    data_38 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/div")[0])
    data_39 = get_text(tree.xpath("/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/table[1]/tbody/tr[2]/td/span/span")[0])
    data_40 = get_text(tree.xpath("/html/body/div[1]/div/div/header/div/div[2]/div/div[4]/div[2]/nav[1]/form/div[1]/label")[0])
    
    scraped_data.append([data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_