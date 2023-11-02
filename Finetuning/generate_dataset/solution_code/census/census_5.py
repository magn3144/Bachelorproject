import csv
from lxml import etree

# Define the HTML elements and XPaths
elements = [
    {
        "element": '<p class="uscb-email-subscription-text uscb-margin-T-0 uscb-margin-B-30">To sign up for updates please enter your email add</p>',
        "xpath": '/html/body/div[3]/div/div/div[11]/footer/div/div[1]/div/p[2]'
    },
    {
        "element": '<p class="uscb-footer-text">Support</p>',
        "xpath": '/html/body/div[3]/div/div/div[11]/footer/div/div[2]/div[1]/div[1]/div[2]/div/a[2]/p'
    },
    {
        "element": '<span class="uscb-header-search-placeholder">Search data, events, resources, and more</span>',
        "xpath": '/html/body/div[3]/div/div/div[3]/header/div[1]/div[2]/div[2]/div[2]/span'
    },
    {
        "element": '<span class="uscb-tag-label uscb-tag-label">Dataset</span>',
        "xpath": '/html/body/div[3]/div/div/div[8]/div/div/div/div[1]/div[2]/a[28]/div/span'
    },
    {
        "element": '<title id="banner-lock-title-default">Lock</title>',
        "xpath": '/html/body/div[3]/div/div/div[1]/div/section/div/div/div/div[2]/div/p/span/svg/title'
    },
    {
        "element": '<div class="uscb-default-x-column-content uscb-body-small-01">View and download 2021 school district estimates f</div>',
        "xpath": '/html/body/div[3]/div/div/div[8]/div/div/div/div[1]/div[2]/a[6]/div/div[3]'
    },
    {
        "element": '<div class="uscb-default-x-column-title uscb-heading-2">SAIPE Model Input Data</div>',
        "xpath": '/html/body/div[3]/div/div/div[8]/div/div/div/div[1]/div[2]/a[5]/div/div[1]'
    },
    {
        "element": '<a class="uscb-header-panel-content-link">                                American Communit</a>',
        "xpath": '/html/body/div[3]/div/div/div[3]/header/div[3]/div/div[4]/div[9]/div[2]/a[3]'
    },
    {
        "element": '<a class="uscb-header-mainnav-tab-title">Data &amp; Maps</a>',
        "xpath": '/html/body/div[3]/div/div/div[3]/header/div[1]/div[2]/div[2]/div[1]/div[2]/a'
    },
    {
        "element": '<h1 class="cmp-title__text">Census Datasets</h1>',
        "xpath": '/html/body/div[3]/div/div/div[6]/div/h1'
    },
    {
        "element": '<label class="ui-helper-hidden-accessible">Enter your email address</label>',
        "xpath": '/html/body/div[3]/div/div/div[11]/footer/div/div[1]/form/label'
    },
    {
        "element": '<p class="usa-banner__header-text">                            An official website o</p>',
        "xpath": '/html/body/div[3]/div/div/div[1]/div/section/div/header/div/div[2]/p[1]'
    },
    {
        "element": '<p class="uscb-sub-heading-2 uscb-color-primary uscb-margin-TB-5" id="currentPageSpan_List_1180774949">1</p>',
        "xpath": '/html/body/div[3]/div/div/div[8]/div/div/div/nav[1]/ul/li[3]/p'
    },
    {
        "element": '<span class="rate-thankyouText">Thank you for your feedback.</span>',
        "xpath": '/html/body/div[3]/div/div/div[11]/div[1]/div[4]/div[2]/span[1]'
    },
    {
        "element": '<span class="uscb-footer-link-separator">|</span>',
        "xpath": '/html/body/div[3]/div/div/div[11]/footer/div/div[2]/div[2]/span[7]'
    },
    {
        "element": '<div class="uscb-default-x-column-title uscb-heading-2">2020 State &amp; Local Government Finance Historical D</div>',
        "xpath": '/html/body/div[3]/div/div/div[8]/div/div/div/div[1]/div[2]/a[35]/div/div[1]'
    },
    {
        "element": '<div class="uscb-author-text-wrapper uscb-meta-data-text">December 2021</div>',
        "xpath": '/html/body/div[3]/div/div/div[8]/div/div/div/div[1]/div[2]/a[13]/div/div[2]/div'
    },
    {
        "element": '<a class="uscb-header-overlay-item-link-sub">                                Spotlights      </a>',
        "xpath": '/html/body/div[3]/div/div/div[3]/header/div[2]/div[1]/div/div[4]/div[3]/div[2]/a[3]'
    },
    {
        "element": '<a class="uscb-pagination-item">						10					</a>',
        "xpath": '/html/body/div[3]/div/div/div[8]/div/div/div/nav[2]/ul/li[12]/a'
    },
    {
        "element": '<p class="uscb-footer-tag-line">Measuring America\'s People, Places, and Economy</p>',
        "xpath": '/html/body/div[3]/div/div/div[11]/footer/div/div[3]/p'
    },
    {
        "element": '<p class="uscb-footer-text-title">Stay Current</p>',
        "xpath": '/html/body/div[3]/div/div/div[11]/footer/div/div[2]/div[1]/div[1]/div[1]/p'
    },
    {
        "element": '<span id="uscb-automation-lastmodified-date">Page Last Revised - October 11, 2023</span>',
        "xpath": '/html/body/div[3]/div/div/div[10]/div/div[1]/div/span'
    },
    {
        "element": '<span class="rate-start-text">255 characters maximum</span>',
        "xpath": '/html/body/div[3]/div/div/div[11]/div[1]/div[3]/div[3]/div[2]/span[1]'
    },
    {
        "element": '<div class="uscb-default-x-column-title uscb-heading-2">County Business Patterns: 2020</div>',
        "xpath": '/html/body/div[3]/div/div/div[8]/div/div/div/div[1]/div[2]/a[8]/div/div[1]'
    },
    {
        "element": '<div class="uscb-author-text-wrapper uscb-meta-data-text">2022</div>',
        "xpath": '/html/body/div[3]/div/div/div[8]/div/div/div/div[1]/div[2]/a[9]/div/div[2]/div'
    },
    {
        "element": '<a class="uscb-header-overlay-item-link-sub">                                Age and Sex     </a>',
        "xpath": '/html/body/div[3]/div/div/div[3]/header/div[2]/div[1]/div/div[1]/div[3]/div[1]/a[1]'
    },
    {
        "element": '<a>NAICS Codes</a>',
        "xpath": '/html/body/div[3]/div/div/div[3]/header/div[1]/div[2]/div[1]/div[2]/div/a[2]'
    },
    {
        "element": '<p>Data files, for public use, with all personally id</p>',
        "xpath": '/html/body/div[3]/div/div/div[7]/div/p'
    },
    {
        "element": '<p class="uscb-sub-heading-2 uscb-color-primary uscb-margin-TB-5">  of  17</p>',
        "xpath": '/html/body/div[3]/div/div/div[8]/div/div/div/nav[1]/ul/li[4]/p'
    },
    {
        "element": '<span class="uscb-tag-label uscb-tag-label">Dataset</span>',
        "xpath": '/html/body/div[3]/div/div/div[8]/div/div/div/div[1]/div[