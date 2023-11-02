from bs4 import BeautifulSoup
import csv

# Open the HTML file
with open("downloaded_pages/investing.html", "r") as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find all the stock prices
stocks = soup.select("td.datatable_cell__LJp3C.datatable_cell--align-end__qgxDQ")
prices = [stock.get_text() for stock in stocks]

# Write the scraped data to a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Price"])
    writer.writerows(zip(range(1, len(prices)+1), prices))