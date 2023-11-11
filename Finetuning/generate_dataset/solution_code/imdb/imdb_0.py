import csv
from lxml import etree

# Define the HTML elements and their corresponding XPaths
html_elements = [
    {
        'element': 'span',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[207]/div[2]/div/div/span/div/button/span/span'
    },
    {
        'element': 'div',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[2]/div/div/div[1]/div'
    },
    {
        'element': 'div',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[4]/div[2]/div'
    },
    {
        'element': 'h3',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[136]/div[2]/div/div/div[1]/a/h3'
    },
    {
        'element': 'h3',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[55]/div[2]/div/div/div[1]/a/h3'
    },
    {
        'element': 'h1',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[1]/div/div[2]/hgroup/h1'
    },
    {
        'element': 'label',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[3]/div/span/label'
    },
    {
        'element': 'p',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/p'
    },
    {
        'element': 'li',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/ul/li[2]'
    },
    {
        'element': 'li',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[2]/div/div/div[1]/ul/li[2]'
    },
    {
        'element': 'a',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/a'
    },
    {
        'element': 'a',
        'xpath': '/html/body/div[2]/footer/div[3]/div[1]/div[3]/ul/li[6]/div/a[2]'
    },
    {
        'element': 'title',
        'xpath': '/html/body/div[2]/footer/div[3]/div[2]/svg/title'
    },
    {
        'element': 'span',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[179]/div[2]/div/div/div[2]/span[1]'
    },
    {
        'element': 'div',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[4]/div/div/div[1]/div'
    },
    {
        'element': 'div',
        'xpath': '/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/label/span/li/span[1]/div[1]'
    },
    {
        'element': 'h3',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[66]/div[2]/div/div/div[1]/a/h3'
    },
    {
        'element': 'h3',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[200]/div[2]/div/div/div[1]/a/h3'
    },
    {
        'element': 'label',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[2]/span/div/span/div/span/label'
    },
    {
        'element': 'li',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/ul/li[3]'
    },
    {
        'element': 'li',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[5]/div/div/div[1]/ul/li[2]'
    },
    {
        'element': 'a',
        'xpath': '/html/body/div[2]/footer/div[3]/div[1]/div[3]/ul/li[5]/a'
    },
    {
        'element': 'span',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[168]/div[2]/div/div/span/div/span/span'
    },
    {
        'element': 'div',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[1]/div/div/div[1]/div'
    },
    {
        'element': 'div',
        'xpath': '/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/label/span/li/span[1]/div[2]'
    },
    {
        'element': 'h3',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[9]/div[2]/div/div/div[1]/a/h3'
    },
    {
        'element': 'h3',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[154]/div[2]/div/div/div[1]/a/h3'
    },
    {
        'element': 'label',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[3]/div/span/span/label'
    },
    {
        'element': 'li',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[4]/ul/li[1]'
    },
    {
        'element': 'li',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div[2]/div[3]/div/div/div[1]/ul/li[1]'
    },
    {
        'element': 'a',
        'xpath': '/html/body/div[2]/footer/div[3]/div[1]/div[3]/ul/li[4]/a'
    },
    {
        'element': 'span',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[205]/div[2]/div/div/div[2]/span[3]'
    },
    {
        'element': 'div',
        'xpath': '/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/a/span[1]/div/div'
    },
    {
        'element': 'h3',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[1]/div/div[1]/div[1]/hgroup/h3'
    },
    {
        'element': 'li',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[228]/div[2]/div/div/div[1]/a/h3'
    },
    {
        'element': 'h3',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[1]/div/div[1]/div[1]/hgroup/h3'
    },
    {
        'element': 'li',
        'xpath': '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[228]/div[2]/div/div/div[1]/a/h3'
    }
]

