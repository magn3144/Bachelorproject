import csv
from lxml import etree
import pandas as pd

# Load the HTML file
html_file = "downloaded_pages/walmart.html"
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# Create an ElementTree object
tree = etree.HTML(html)

# Define the target HTML elements and their XPaths
elements = [
    {
        "name": "Brussels Sprouts & Cabbage",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[1]/div/div/section[2]/ul/li[2]/ul/li[4]/a"
    },
    {
        "name": "Thanksgiving",
        "xpath": "/html/body/div/div[1]/div/div/div[1]/div/div[1]/section[2]/nav/ul/li[3]/a"
    },
    {
        "name": "Address",
        "xpath": "/html/body/div/div[1]/div/div/div[1]/div/div[1]/section[1]/div/div/div/div[1]/div/div[2]/div/button/div[1]/div[1]/div[2]/div[2]/div"
    },
    {
        "name": "Price",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[2]/section/section/div/ul/li[1]/div/div[4]/div[3]"
    },
    {
        "name": "Salad Name",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[5]/section/section/div/ul/li[15]/div/span/span/span"
    },
    {
        "name": "Unit",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[2]/section/section/div/ul/li[17]/div/div[4]/div[2]/span"
    },
    {
        "name": "Category",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/span/h1"
    },
    {
        "name": "Subcategory",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[3]/div/div/div/section/div/div/h2[2]"
    },
    {
        "name": "New in produce",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[5]/section/section/header/section/div/div/div/h2"
    },
    {
        "name": "Product 1",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[5]/section/section/div/ul/li[12]/div/a/span/h3"
    },
    {
        "name": "Product 2",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[2]/section/section/div/ul/li[14]/div/a/span/h3"
    },
    {
        "name": "Description",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/section/div/div[1]/article/a/div/p"
    },
    {
        "name": "Alternative Category",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[1]/div/div/section[2]/ul/li[9]/ul/li[2]/a"
    },
    {
        "name": "Grocery & Essentials",
        "xpath": "/html/body/div/div[1]/div/div/div[1]/div/div[1]/section[2]/nav/ul/li[2]/a"
    },
    {
        "name": "Shipping Information",
        "xpath": "/html/body/div/div[1]/div/div/div[1]/div/div[1]/section[1]/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/div[2]/div[1]/div"
    },
    {
        "name": "Price2",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[2]/section/section/div/ul/li[17]/div/div[4]/div[1]"
    },
    {
        "name": "Apple Name",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[2]/section/section/div/ul/li[6]/div/span/span/span"
    },
    {
        "name": "Add Button",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[3]/section/section/div/ul/li[5]/div/div[2]/div[2]/div/button/span"
    },
    {
        "name": "App Compatibility",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[3]/div/div/div/section/div/div/h2[4]"
    },
    {
        "name": "Peak Season",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[2]/section/section/header/section/div/div/div/h2"
    },
    {
        "name": "Salad Kit Name",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[5]/section/section/div/ul/li[16]/div/a/span/h3"
    },
    {
        "name": "Grapes Name",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[1]/div/div/section[2]/div[2]/div[3]/article/a/div/h3"
    },
    {
        "name": "Melon Description",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[3]/div/div/div/section/div/div/p[6]"
    },
    {
        "name": "Footer Link",
        "xpath": "/html/body/div/div[1]/div/div/span/footer/section[2]/ul/li[19]/a"
    },
    {
        "name": "Berries",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[1]/div/div/section[2]/ul/li[1]/ul/li[5]/a"
    },
    {
        "name": "Footer Info",
        "xpath": "/html/body/div/div[1]/div/div/span/footer/section[2]/div"
    },
    {
        "name": "Price3",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[5]/section/section/div/ul/li[3]/div/div[4]/div[2]"
    },
    {
        "name": "Availability",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[5]/section/section/div/ul/li[14]/div/div[6]/span[1]"
    },
    {
        "name": "Pickup",
        "xpath": "/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[3]/section/section/div/ul/li[5]/div/div[2]/div[2]/div/button/span"
    },
    {
        "name": "Fresh Apples",
        "xpath": "/html/body/div/div[1]/div/div/div