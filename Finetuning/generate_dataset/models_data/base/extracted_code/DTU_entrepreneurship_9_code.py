

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.dtu.dk/en/entrepreneurship"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

department_name = soup.find("h2", class_="a-heading-h1 o-hero__title").text.strip()
department_link = soup.find("a", class_="servicemenu__link-text").get("href")

print(department_name)
print(department_link)

df = pd.DataFrame({"Department Name": department_name, "Department Link": department_link})
df.to_csv("scraped_data.csv", index=False)

