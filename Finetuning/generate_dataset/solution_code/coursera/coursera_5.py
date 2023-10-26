import csv
import os
from lxml import etree

def extract_program_names():
    html_file = "downloaded_pages/coursera.html"

    with open(html_file, "rb") as file:
        tree = etree.parse(file)

    program_elements = tree.xpath("//div[@class='_mml263m megaMenuGoalItem-name']")
    
    program_names = []
    for element in program_elements:
        program_names.append(element.text.strip())

    return program_names

def save_to_csv(data):
    csv_file = "scraped_data.csv"

    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Program Name"])
        writer.writerows(data)

if __name__ == "__main__":
    program_names = extract_program_names()
    save_to_csv(program_names)