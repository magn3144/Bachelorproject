import csv
from pathlib import Path
from bs4 import BeautifulSoup

# Define the HTML elements and their corresponding XPaths
elements = [
    {
        "element": "a",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[2]/ul/li[6]/a"
    },
    {
        "element": "a",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[2]/section/div[3]/div[1]/div/div[2]/span[2]/ol/li[2]/a"
    },
    {
        "element": "span",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/h1/div[3]/a/span"
    },
    {
        "element": "span",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div/label[48]/div/span/div/span"
    },
    {
        "element": "div",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[35]/div/div[2]/div/div/div/div/div/div[2]/div[1]"
    },
    {
        "element": "div",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[24]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div"
    },
    {
        "element": "h2",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[1]/div/div/div/div/h2"
    },
    {
        "element": "h2",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/span/h2"
    },
    {
        "element": "h3",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[2]/h3"
    },
    {
        "element": "a",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/ul/li[6]/a"
    },
    {
        "element": "a",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[1]/ul/li[2]/a"
    },
    {
        "element": "span",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/h1/div[2]/div/a/span"
    },
    {
        "element": "span",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div/label[34]/div/span/div/span"
    },
    {
        "element": "div",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[1]"
    },
    {
        "element": "div",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[32]/div/div[2]/div/div/div/div/div/div[2]/div[1]"
    },
    {
        "element": "h3",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/h3"
    },
    {
        "element": "a",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[1]/ul/li[6]/a"
    },
    {
        "element": "a",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[1]/ul/li[5]/a"
    },
    {
        "element": "span",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/h1/div[1]/a/span"
    },
    {
        "element": "span",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[3]/span/span"
    },
    {
        "element": "div",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[7]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div"
    },
    {
        "element": "h3",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[1]/h3"
    },
    {
        "element": "a",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[2]/ul/li[1]/a"
    },
    {
        "element": "span",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[19]/div/div[2]/div/div/div/div/div/div[2]/span/span[2]"
    },
    {
        "element": "div",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div[1]/div[3]/div[1]/div/div/div[2]"
    },
    {
        "element": "a",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/ul/li[1]/a"
    },
    {
        "element": "span",
        "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div/label[20]/div/span/div/span"
    },
    {
      "element": "div",
      "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div/label[26]/div/span/div/span"
    },
    {
      "element": "div",
      "xpath": "/html/body/div[5]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[1]/div/manage-listings-summary-view-topbar/div/span/span/a/span"
    }
]

# Specify the local path to the HTML file
html_file_path = "downloaded_pages/airbnb.html"

# Define the category
category = "Tourism"

# Define the task description
task = "Gather inspiration for future