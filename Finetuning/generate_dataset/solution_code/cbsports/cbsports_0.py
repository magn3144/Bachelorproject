import csv
from lxml import etree

# Define the target HTML file
html_path = 'downloaded_pages/cbsports.html'

# Define the list of web-scraping tasks
tasks = [
    {
        'xpath': '/html/body/div[4]/div[1]/footer/div[1]/div/div[1]/div/ul/li[6]/a',
        'task': 'Extract text from <a> WPST Gear',
    },
    {
        'xpath': '/html/body/div[4]/div[1]/footer/div[2]/div/div[3]/small[2]/a',
        'task': 'Extract text from <a> Powered by Shopify',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[27]/div/a/span',
        'task': 'Extract text from <span> Men\'s Primaloft Hooded Jacket',
    },
    {
        'xpath': '/html/body/div[3]/div/header/div/nav/ul/li[8]/div/ul/li[1]/a/span',
        'task': 'Extract text from <span> Evershield',
    },
    {
        'xpath': '/html/body/div[2]/div/h2',
        'task': 'Extract text from <h2> Just added to your cart',
    },
    {
        'xpath': '/html/body/div[3]/div/header/nav/ul/li[11]/form/label',
        'task': 'Extract text from <label> Currency',
    },
    {
        'xpath': '/html/body/ul[1]/li[1]',
        'task': 'Extract text from <li> Choosing a selection results in a full page refresh',
    },
    {
        'xpath': '/html/body/div[3]/div/header/nav/ul/li[8]/ul/li[1]',
        'task': 'Extract text from <li> Technology Menu',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[27]/div/div[2]',
        'task': 'Extract text from <div> Men\'s Primaloft Hooded Jacket',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[15]/div/div[2]',
        'task': 'Extract text from <div> Men\'s Lightweight Bomber',
    },
    {
        'xpath': '/html/body/div[4]/div[1]/footer/div[1]/div/div[4]/div/p',
        'task': 'Extract text from <p> Newsletter',
    },
    {
        'xpath': '/html/body/div[4]/div[1]/footer/div[1]/div/div[1]/div/ul/li[2]/a',
        'task': 'Extract text from <a> Our Story',
    },
    {
        'xpath': '/html/body/a',
        'task': 'Extract text from <a class="in-page-link visually-hidden skip-link"> Skip to content',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[9]/div/dl/div[4]/dd/span',
        'task': 'Extract text from <span class="price-item price-item--regular"> Coming Soon',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[27]/div/dl/div[4]/dt/span',
        'task': 'Extract text from <span class="visually-hidden visually-hidden--inline"> Availability',
    },
    {
        'xpath': '/html/body/div[3]/div/header/div/div[2]/div/form/label',
        'task': 'Extract text from <label class="visually-hidden"> Currency',
    },
    {
        'xpath': '/html/body/ul[1]/li[2]',
        'task': 'Extract text from <li> Press the space key then arrow keys to make a selection',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[2]/li[2]',
        'task': 'Extract text from <li class="pagination__text"> Page 1 of 2',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[3]/div/div[2]',
        'task': 'Extract text from <div class="h4 grid-view-item__title product-card__title"> Men\'s 3-Snap Pouch Pullover',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[10]/div/div[2]',
        'task': 'Extract text from <div class="h4 grid-view-item__title product-card__title"> Men\'s Lightweight Bomber',
    },
    {
        'xpath': '/html/body/div[4]/div[1]/footer/div[1]/div/div[2]/div/p',
        'task': 'Extract text from <p class="h4"> Join the fun',
    },
    {
        'xpath': '/html/body/div[4]/div[1]/footer/div[1]/div/div[1]/div/ul/li[10]/a',
        'task': 'Extract text from <a> Contact Us',
    },
    {
        'xpath': '/html/body/div[4]/div[1]/footer/div[2]/div/div[3]/small[1]/a',
        'task': 'Extract text from <a> CB Sports',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[16]/div/a/span',
        'task': 'Extract text from <span class="visually-hidden"> Men\'s Double Stripe Bomber',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[30]/div/dl/div[1]/dt/span',
        'task': 'Extract text from <span class="visually-hidden visually-hidden--inline"> Regular price',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/header/div[2]/div/div/div[1]/div[2]/label',
        'task': 'Extract text from <label class="filters-toolbar__label select-label"> Sort by',
    },
    {
        'xpath': '/html/body/ul[2]/li[3]',
        'task': 'Extract text from <li id="a11y-new-window-external-message"> Opens external website in a new window.',
    },
    {
        'xpath': '/html/body/ul[2]/li[2]',
        'task': 'Extract text from <li id="a11y-external-message"> Opens external website.',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[5]/div/div[2]',
        'task': 'Extract text from <div class="h4 grid-view-item__title product-card__title"> Men\'s 3-Snap Pouch Pullover',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[12]/div/div[2]',
        'task': 'Extract text from <div class="h4 grid-view-item__title product-card__title"> Men\'s Lightweight Bomber',
    },
    {
        'xpath': '/html/body/div[4]/div[1]/footer/div[1]/div/div[3]/div/p',
        'task': 'Extract text from <p class="h4"> Size Charts',
    },
    {
        'xpath': '/html/body/div[4]/div[1]/footer/div[1]/div/div[1]/div/ul/li[4]/a',
        'task': 'Extract text from <a> Women\'s',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[23]/div/a/span',
        'task': 'Extract text from <span class="visually-hidden"> Men\'s Snap Front Windbreaker',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/div/ul[1]/li[5]/div/dl/div[3]/dt/span',
        'task': 'Extract text from <span class="visually-hidden visually-hidden--inline"> Unit price',
    },
    {
        'xpath': '/html/body/div[4]/main/div/div/header/div[2]/div/div/div[1]/div[1]/label',
        'task': 'Extract text from <label class="filters-toolbar__label select-label"> Filter by',
    },
    {
        'xpath': '/html/body/ul[2]/li[1]',
        'task': 'Extract text