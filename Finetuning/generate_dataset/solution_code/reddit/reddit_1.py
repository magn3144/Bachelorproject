import csv
from lxml import html

def extract_text(element):
    text = element.text_content().strip()
    return text

def extract_xpath_data(xpath, tree):
    element = tree.xpath(xpath)
    if element:
        return extract_text(element[0])
    else:
        return ""

def scrape_html_data():
    path = "downloaded_pages/reddit.html"
    with open(path, "r") as file:
        content = file.read()
        
    tree = html.fromstring(content)
    
    data = {}
    
    data["Title"] = extract_xpath_data("/html/head/title", tree)
    data["Flipping at the Grand Exchange"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[6]/div/div/div/div[2]/div[2]/div[1]/span[2]/div/span", tree)
    data["Liquidated Jensen Huang"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[184]/div/div/div/div[2]/div[2]/div[1]/span[2]/div/span", tree)
    data["View discussions in 1 other community"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[4]/a", tree)
    data["2 days ago"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[138]/div/div/div/div[2]/div[2]/div[1]/span/a", tree)
    data["Only Crypto Allowed is BTC and ETH"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[4]/div/div[2]/div[8]/div/div[2]/div", tree)
    data["Table"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/span[17]/button/div/div", tree)
    data["Update on $50k NVDA Puts"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[1]/div/div/div/div[3]/div[1]/div/h1", tree)
    data["Put means you make money if the stock (in this cas"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[103]/div/div/div/div[2]/div[2]/div[2]/div/p", tree)
    data["Luck is a hell of a drug"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[190]/div/div/div/div[2]/div[2]/div[2]/div/p", tree)
    data["325"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/div[2]/div/div/div/table/tbody/tr[4]/td[2]", tree)
    data["About Community"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/div[1]/h2", tree)
    data["-"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/div[2]/div/div/div/table/thead/tr/th[5]", tree)
    data["Flipping at the Grand Exchange"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[5]/div/div[2]/div[4]/div/span", tree)
    data[" · "] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[142]/div/div/div/div[2]/div[2]/div[1]/span/span", tree)
    data["r/wallstreetbets"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[47]/div/div/div/div[2]/div[2]/div[2]/div/p[1]/a[1]", tree)
    data["2 days ago"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div[1]/span/a", tree)
    data["Don't Shit on the Community"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[4]/div/div[2]/div[12]/div/div[2]/div", tree)
    data["20"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[90]/div/div/div/div[2]/div[2]/div[3]/div[1]/div", tree)
    data["Fuck you it's my money and I'll spend it how ever"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[5]/div/div/div/div[2]/div[2]/div[2]/div/p", tree)
    data["Nah"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[135]/div/div/div/div[2]/div[2]/div[2]/div/p", tree)
    data["9"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td[2]", tree)
    data["r/wallstreetbets Rules"] = extract_xpath_data("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[5]/div/div[2]/div[4]/div/span", tree)
    
    with open("scraped_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        writer.writerow(data.values())

scrape_html_data()