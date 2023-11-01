import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def scrape_data(html_file, xpath_list):
    driver = webdriver.Chrome()
    driver.get(f"file://{html_file}")

    scraped_data = []

    for element, xpath in xpath_list:
        try:
            element_text = driver.find_element(By.XPATH, xpath).text
            scraped_data.append((element, element_text))
        except:
            scraped_data.append((element, None))

    driver.quit()

    return scraped_data

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Element', 'Text'])
        writer.writerows(data)

if __name__ == "__main__":
    xpath_list = [
        ('Marketplace Spring Fling Sale', '/html/body/div[1]/div[1]/a/span[1]'),
        ('Newsletter', '/html/body/div[1]/nav/div[1]/ul/li[5]/div/ul/li[5]/a/span'),
        ('Currency Code', '/html/body/div[1]/nav/ul/ul[2]/li[3]/button/span/div[1]'),
        ('Sign In', '/html/body/div[1]/div[3]/div/div/div[1]/div[2]/h3'),
        ('Password Label', '/html/body/div[1]/div[3]/div/div/div[1]/form/div[2]/div/div[1]/label'),
        ('Sign In Link', '/html/body/div[1]/div[4]/div/div/div[2]/a'),
        ('Lead Text', '/html/body/div[1]/div[4]/div/div/div[1]/p'),
        ('Currency', '/html/body/div[1]/nav/div[1]/ul/li[6]/div/ul/li[3]/button/span[2]'),
        ('Currency Code', '/html/body/div[1]/nav/div[1]/ul/li[6]/button/span/div[1]'),
        ('Email Label', '/html/body/div[1]/div[3]/div/div/div[1]/form/div[1]/label'),
        ('Sign Up Link', '/html/body/div[1]/div[3]/div/div/div[2]/a'),
        ('Challenges', '/html/body/div[1]/nav/ul/ul[1]/li[3]/div/ul/li[2]/a/span'),
        ('Forgot Password Link', '/html/body/div[1]/div[3]/div/div/div[1]/form/div[2]/div/div[2]/a'),
        ('Marketplace', '/html/body/div[1]/nav/div[1]/ul/li[3]/div/ul/li[1]/a/span[1]')
    ]

    scraped_data = scrape_data('downloaded_pages/artstation.html', xpath_list)
    save_to_csv(scraped_data)