from lxml import etree
import csv

# Load the HTML file
html_path = "downloaded_pages/bodybuilding.html"
with open(html_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Create the HTML tree
tree = etree.HTML(html_content)

# Define the workout plan names and their corresponding XPaths
workout_plan_names = [
    "Kris Gethin Muscle Building",
    "Your Transformation Starts Here Volume 2",
    "Foundations of Nutrition",
    "Serious Strength in 8 Weeks",
    "Full-Body Weight-Loss Home Workouts",
    "Livefit",
    "Muscle Building"
]
xpaths = [
    "/html/body/section/main/div[3]/div[2]/div/div/div/div/div[2]/div/div[29]/figure/a/figcaption/div[1]/span",
    "/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[5]/figure/a/figcaption/div[1]/span",
    "/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[31]/figure/a/figcaption/div[1]/span",
    "/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[22]/figure/a/figcaption/div[1]/span",
    "/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[20]/figure/a/figcaption/div[1]/span",
    "/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[18]/figure/a/figcaption/div[1]/span",
    "/html/body/section/main/div[3]/div[1]/div/h2"
]

# Prepare the data for CSV writing
data = zip(workout_plan_names, xpaths)

# Save the scraped data as a CSV file
csv_path = "scraped_data.csv"
with open(csv_path, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Workout Plan Name", "XPath"])
    writer.writerows(data)