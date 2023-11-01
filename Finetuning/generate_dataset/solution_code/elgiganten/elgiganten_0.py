import csv
from lxml import etree

# Define the XPaths for the HTML elements
xpaths = {
    "databeskyttelsespolitik": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/div[2]/elk-navigation/div/mat-expansion-panel[1]/div/div/div/ul/li[5]/a",
    "kundeservice": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/div[2]/elk-navigation/div/mat-expansion-panel[1]/div/div/div/ul/li[1]/a",
    "antal_varer": "/html/body/header/div[5]/div/div[5]/label/span/span[1]",
    "gaming": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[1]/elk-category-carousel/elk-image-slider/elk-carousel/div/swiper/div/div[6]/elk-image-title-element/a/span",
    "returret": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/elk-lib-icon-bar/div/div[4]/a/div/div",
    "indkoebskurv": "/html/body/header/div[5]/div/div[5]/label/div",
    "produkter_til_lavere_priser": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[4]/elk-content-carousel/div/elk-carousel/div/swiper/div/div[3]/elk-content-carousel-element/a/h3",
    "maanedens_gaming_gear": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[4]/elk-content-carousel/div/elk-carousel/div/swiper/div/div[1]/elk-content-carousel-element/a/h3",
    "elgiganten_a_s": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/div[2]/elk-footer-logo/div/div[2]/p[1]",
    "lad_elektronikken_koere_i_ring": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[6]/elk-content-carousel/div[1]/h2",
    "salgs_og_leveringsbetingelser": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/div[2]/elk-footer-logo/div/div[2]/p[2]/a[1]",
    "kategorier": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/div[2]/elk-footer-logo/div/div[2]/p[2]/a[2]",
    "hjem_rengoering_koekkenudstyr": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[1]/elk-category-carousel/elk-image-slider/elk-carousel/div/swiper/div/div[4]/elk-image-title-element/a/span",
    "epoq_koekken_bryggers": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[1]/elk-category-carousel/elk-image-slider/elk-carousel/div/swiper/div/div[7]/elk-image-title-element/a/span",
    "inspiration": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/div[2]/elk-navigation/div/mat-expansion-panel[3]/mat-expansion-panel-header/span/mat-panel-title/div",
    "koeb_med_delbetaling": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[4]/elk-content-carousel/div/elk-carousel/div/swiper/div/div[4]/elk-content-carousel-element/h3",
    "rabat_paa_udval": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[4]/elk-content-carousel/div/elk-carousel/div/swiper/div/div[2]/elk-content-carousel-element/a/div/div/p",
    "whistleblowing_i_organisationen": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/div[2]/elk-navigation/div/mat-expansion-panel[2]/div/div/div/ul/li[10]/a",
    "varehuse_aabningstider": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/div[2]/elk-navigation/div/mat-expansion-panel[1]/div/div/div/ul/li[2]/a",
    "mobil_tablet_smartwatch": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[1]/elk-category-carousel/elk-image-slider/elk-carousel/div/swiper/div/div[3]/elk-image-title-element/a/span",
    "hvidevarer": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[1]/elk-category-carousel/elk-image-slider/elk-carousel/div/swiper/div/div[2]/elk-image-title-element/a/span",
    "prismatch": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/elk-lib-icon-bar/div/div[3]/a/div/div",
    "elgigantens_kundeklub": "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[4]/elk-content-carousel/div/elk-carousel/div/swiper/div/div[6]/elk-content-carousel-element/h3"
}

# Function to scrape the text content based on the given xpath
def scrape_data(html_file_path, xpath):
    with open(html_file_path, "rb") as file:
        tree = etree.parse(file)
        element = tree.xpath(xpath)
        if element:
            return element[0].text.strip()
        else:
            return ""

# Create a list of web-scraping tasks
scraping_tasks = []
for key, value in xpaths.items():
    task = {"element": key, "xpath": value, "data": scrape_data("downloaded_pages/elgiganten.html", value)}
    scraping_tasks.append(task)

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["element", "xpath", "data"])
    writer.writeheader()
    writer.writerows(scraping_tasks)