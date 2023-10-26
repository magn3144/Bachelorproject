import csv
import re
from lxml import etree

def get_category(element):
    category_match = re.search(r'categories\/(.+?)\/', element)
    if category_match:
        return category_match.group(1)
    return None

filename = 'downloaded_pages/cbsports.html'

tree = etree.parse(filename)
root = tree.getroot()

category = None

for element, xpath in [
    ('<a>                          WPST Gear             </a>', '/html/body/div[4]/div[1]/footer/div[1]/div/div[1]/div/ul/li[6]/a'),
    ('<a>Powered by Shopify</a>', '/html/body/div[4]/div[1]/footer/div[2]/div/div[3]/small[2]/a'),
    ('<span class="visually-hidden">Men\'s Primaloft Hooded Jacket</span>', '/html/body/div[4]/main/div/div/div/ul[1]/li[27]/div/a/span'),
    ('<span class="site-nav__label">Evershield</span>', '/html/body/div[3]/div/header/div/nav/ul/li[8]/div/ul/li[1]/a/span'),
    ('<h2 class="cart-popup__heading" id="CartPopupHeading">Just added to your cart</h2>', '/html/body/div[2]/div/h2'),
    ('<label class="currency-selector__label">Currency</label>', '/html/body/div[3]/div/header/nav/ul/li[11]/form/label'),
    ('<li id="a11y-refresh-page-message">Choosing a selection results in a full page refres</li>', '/html/body/ul[1]/li[1]'),
    ('<li class="visually-hidden">Technology Menu</li>', '/html/body/div[3]/div/header/nav/ul/li[8]/ul/li[1]'),
    ('<div class="h4 grid-view-item__title product-card__title">Men\'s Primaloft Hooded Jacket</div>', '/html/body/div[4]/main/div/div/div/ul[1]/li[27]/div/div[2]'),
    ('<div class="h4 grid-view-item__title product-card__title">Men\'s Lightweight Bomber</div>', '/html/body/div[4]/main/div/div/div/ul[1]/li[15]/div/div[2]'),
    ('<p class="h4">Newsletter</p>', '/html/body/div[4]/div[1]/footer/div[1]/div/div[4]/div/p'),
    ('<a>                          Our Story             </a>', '/html/body/div[4]/div[1]/footer/div[1]/div/div[1]/div/ul/li[2]/a'),
    ('<a class="in-page-link visually-hidden skip-link">Skip to content</a>', '/html/body/a'),
    ('<span class="price-item price-item--regular">        Coming Soon      </span>', '/html/body/div[4]/main/div/div/div/ul[1]/li[9]/div/dl/div[4]/dd/span'),
    ('<span class="visually-hidden visually-hidden--inline">Availability</span>', '/html/body/div[4]/main/div/div/div/ul[1]/li[27]/div/dl/div[4]/dt/span'),
    ('<label class="visually-hidden">Currency</label>', '/html/body/div[3]/div/header/div/div[2]/div/form/label'),
    ('<li id="a11y-selection-message">Press the space key then arrow keys to make a sele</li>', '/html/body/ul[1]/li[2]'),
    ('<li class="pagination__text">    Page 1 of 2  </li>', '/html/body/div[4]/main/div/div/div/ul[2]/li[2]'),
    ('<div class="h4 grid-view-item__title product-card__title">Men\'s 3-Snap Pouch Pullover</div>', '/html/body/div[4]/main/div/div/div/ul[1]/li[3]/div/div[2]'),
    ('<div class="h4 grid-view-item__title product-card__title">Men\'s Lightweight Bomber</div>', '/html/body/div[4]/main/div/div/div/ul[1]/li[10]/div/div[2]'),
    ('<p class="h4">Join the fun</p>', '/html/body/div[4]/div[1]/footer/div[1]/div/div[2]/div/p'),
    ('<a>                          Contact Us            </a>', '/html/body/div[4]/div[1]/footer/div[1]/div/div[1]/div/ul/li[10]/a'),
    ('<a>CB Sports</a>', '/html/body/div[4]/div[1]/footer/div[2]/div/div[3]/small[1]/a'),
    ('<span class="visually-hidden">Men\'s Double Stripe Bomber</span>', '/html/body/div[4]/main/div/div/div/ul[1]/li[16]/div/a/span'),
    ('<span class="visually-hidden visually-hidden--inline">Regular price</span>', '/html/body/div[4]/main/div/div/div/ul[1]/li[30]/div/dl/div[1]/dt/span'),
    ('<label class="filters-toolbar__label select-label">Sort by</label>', '/html/body/div[4]/main/div/div/header/div[2]/div/div/div[1]/div[2]/label'),
    ('<li id="a11y-new-window-external-message">Opens external website in a new window.</li>', '/html/body/ul[2]/li[3]'),
    ('<li id="a11y-external-message">Opens external website.</li>', '/html/body/ul[2]/li[2]'),
    ('<div class="h4 grid-view-item__title product-card__title">Men\'s 3-Snap Pouch Pullover</div>', '/html/body/div[4]/main/div/div/div/ul[1]/li[4]/div/div[2]'),
    ('<div class="h4 grid-view-item__title product-card__title">Men\'s Lightweight Bomber</div>', '/html/body/div[4]/main/div/div/div/ul[1]/li[12]/div/div[2]'),
    ('<p class="h4">Size Charts</p>', '/html/body/div[4]/div[1]/footer/div[1]/div/div[3]/div/p'),
    ('<a>                          Women\'s               </a>', '/html/body/div[4]/div[1]/footer/div[1]/div/div[1]/div/ul/li[4]/a'),
    ('<span class="visually-hidden">Men\'s Snap Front Windbreaker</span>', '/html/body/div[4]/main/div/div/div/ul[1]/li[23]/div/a/span'),
    ('<span class="visually-hidden visually-hidden--inline">Unit price</span>', '/html/body/div[4]/main/div/div/div/ul[1]/li[5]/div/dl/div[3]/dt/span'),
    ('<label class="filters-toolbar__label select-label">Filter by</label>', '/html/body/div[4]/main/div/div/header/div[2]/div/div/div[1]/div[1]/label'),
    ('<li id="a11y-new-window-message">Opens in a new window.</li>', '/html/body/ul[2]/li[1]'),
    ('<div class="h4 grid-view-item__title product-card__title">Men\'s 3-Snap Pouch Pullover</div>', '/html/body/div[4]/main/div/div/div/ul[1]/li[5]/div/div[2]'),
    ('<div class="h4 grid-view-item__title product-card__title">Men\'s Lightweight Bomber</div>', '/html/body/div[4]/main/div/div/div/ul[1]/li[11]/div/div[2]'),
    ('<p class="h4">Quick links</p>', '/html/body/div[4]/div[1]/footer/div[1]/div/div[1]/div/p'),
    ('<a>                          Men\'s                 </a>', '/html/body/div[4]/div[1]/footer/div[1]/div/div[1]/div/ul/li[3]/a'),
    ('<span class="visually-hidden">Men\'s Primaloft Hooded Jacket</span>', '/html/body/div[4]/main/div/div/div/ul[1]/li[29]/div/a/span'),
    ('<span>/</span>', '/html/body/div[4]/main