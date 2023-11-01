import csv
from lxml import etree

def scrape_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()
        tree = etree.HTML(content)
        
        data = []
        
        element1 = tree.xpath('/html/body/div[1]/div/div[1]/div/div/div/div[1]/a[2]')
        element2 = tree.xpath('/html/body/div[1]/div/div[2]/main/div/div/a')
        element3 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[6]/div/ul/li[12]/span/span[2]')
        element4 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[5]/div/ul/li[2]/a/span[2]')
        element5 = tree.xpath('/html/body/div[1]/div/div[2]/div/div[2]/div')
        element6 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[1]/section/div[1]/h1')
        element7 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[5]/h2')
        element8 = tree.xpath('/html/body/div[1]/div/div[2]/main/div/div/p')
        element9 = tree.xpath('/html/body/div[1]/div/div[1]/div/div/div/div[1]/a[3]')
        element10 = tree.xpath('/html/body/div[1]/div/div[1]/div/div/div/div[2]/a[1]')
        element11 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[7]/div/ul/li[13]/span/span[2]')
        element12 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[3]/a/span[2]')
        element13 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[3]/h2')
        element14 = tree.xpath('/html/body/div[1]/div/div[2]/main/p/a')
        element15 = tree.xpath('/html/body/div[1]/div/div[3]/div[2]/p/a')
        element16 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[4]/div/ul/li[24]/a/span[2]')
        element17 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[4]/div/ul/li[7]/a/span[2]')
        element18 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[6]/h2')
        element19 = tree.xpath('/html/body/div[1]/div/div[2]/div/div[2]/a')
        element20 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[39]/a/span[2]')
        element21 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[5]/a/span[2]')
        element22 = tree.xpath('/html/body/div[1]/div/div[2]/main/div/div/h2')
        element23 = tree.xpath('/html/body/div[1]/div/div[1]/div/div/div/div[2]/a[2]')
        element24 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[33]/a/span[2]')
        element25 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[7]/div/ul/li[11]/span/span[2]')
        element26 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[2]/h2')
        element27 = tree.xpath('/html/body/div[1]/div/div[1]/div/div/div/div[1]/a[1]')
        element28 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[3]/div/ul/li[2]/a/span[2]')
        element29 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[34]/a/span[2]')
        element30 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[7]/h2')
        element31 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[6]/div/ul/li[20]/span/span[2]')
        element32 = tree.xpath('/html/body/div[1]/div/div[3]/div[2]/ul/li[11]/a/span')
        element33 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[11]/a/span[2]')
        element34 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[19]/a/span[2]')
        element35 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[4]/div/ul/li[21]/a/span[2]')
        element36 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[4]/div/ul/li[18]/a/span[2]')
        element37 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[7]/div/ul/li[16]/span/span[2]')
        element38 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[4]/div/ul/li[11]/a/span[2]')
        element39 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[8]/a/span[2]')
        element40 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[3]/div/ul/li[6]/a/span[2]')
        element41 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[7]/div/ul/li[5]/span/span[2]')
        element42 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[2]/h2')
        element43 = tree.xpath('/html/body/div[1]/div/div[1]/div/div/div/div[1]/a[1]')
        element44 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[3]/div/ul/li[2]/a/span[2]')
        element45 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[7]/div/ul/li[11]/span/span[2]')
        element46 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[6]/h2')
        element47 = tree.xpath('/html/body/div[1]/div/div[2]/main/section[3]/h2')
        
        if len(element1) > 0:
            data.append(element1[0].text)
        if len(element2) > 0:
            data.append(element2[0].text)
        if len(element3) > 0:
            data.append(element3[0].text)
        if len(element4) > 0:
            data.append(element4[0].text)
        if len(element5) > 0:
            data.append(element5[0].text)
        if len(element6) > 0:
            data.append(element6[0].text)
        if len(element7) > 0:
            data.append(element7[0].text)
        if len(element8) > 0:
            data.append(element8[0].text)
        if len(element9) > 0:
            data.append(element9[0].text)
        if len(element10) > 0:
            data.append(element10[0].text)
        if len(element11) > 0:
            data.append(element11[0].text)
        if len(element12) > 0:
            data.append(element12[0].text)
        if len(element13) > 0:
            data.append(element13[0].text)
        if len(element14) > 0:
            data.append(element14[0].text)
        if len(element15) > 0:
            data.append(element15[0].text)
        if len(element16) > 0:
            data.append(element16[0].text)
        if len(element17) > 0:
            data.append(element17[0].text)
        if len(element18) > 0:
            data.append(element18[0].text)
        if