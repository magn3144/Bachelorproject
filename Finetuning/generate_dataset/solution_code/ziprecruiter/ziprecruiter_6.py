import csv

data = [
    {
        'title': '1,970 Programmer Jobs in Oxford, UK | ZipRecruiter',
        'xpath': '/html/head/title'
    },
    {
        'title': 'Software Engineer, Mid-Level About us Pictura Bio',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[8]/div[1]/div/div'
    },
    {
        'title': '19 Oct',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[13]/div[2]'
    },
    {
        'title': 'Global Terms of Use Agreement',
        'xpath': '/html/body/footer/div/div[2]/ul/li[4]/a'
    },
    {
        'title': '20',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/div[3]/ul/li[5]/a'
    },
    {
        'title': 'ZipRecruiter, Inc. © All Rights Reserved Worldwide',
        'xpath': '/html/body/footer/div/div[1]/div/nav[2]/span'
    },
    {
        'title': 'Distance',
        'xpath': '/html/body/main/section/div/form/div[3]/div/a/span'
    },
    {
        'title': 'Get new jobs for this search by email',
        'xpath': '/html/body/main/div/div/div/div/div[1]/div/div[1]/h3'
    },
    {
        'title': 'Contact Us',
        'xpath': '/html/body/footer/div/div[1]/div/nav[1]/div/div[4]/h3'
    },
    {
        'title': 'If you are a human, ignore this field',
        'xpath': '/html/body/main/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/div[1]/label'
    },
    {
        'title': '1,970 Programmer Jobs in Oxford, UK',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/div[1]/div/div/h1'
    },
    {
        'title': 'Footer',
        'xpath': '/html/body/footer/div/div[1]/h2'
    },
    {
        'title': 'Senior Software Engineer Business Area: Lucy Elec',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[18]/div[1]/div/div'
    },
    {
        'title': '10 Oct',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[20]/div[2]'
    },
    {
        'title': 'Global Terms of Use Agreement and acknowledge that you have read and understand the',
        'xpath': '/html/body/main/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/small/div/a[1]'
    },
    {
        'title': 'Suggested Jobs',
        'xpath': '/html/body/nav/div/div[2]/ul/li[1]/a'
    },
    {
        'title': 'ZipRecruiter UK Ltd., c/o Fieldfisher LLP Riverban',
        'xpath': '/html/body/footer/div/div[1]/div/nav[3]/span'
    },
    {
        'title': 'Annually',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[9]/div[1]/div/div[1]/div/span'
    },
    {
        'title': 'For Job Seekers',
        'xpath': '/html/body/footer/div/div[1]/div/nav[1]/div/div[1]/h3'
    },
    {
        'title': 'Lead LabVIEW Developer Location: Oxfordshire Sala',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[19]/div[1]/div/div'
    },
    {
        'title': '14 Oct',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[3]/div[2]'
    },
    {
        'title': 'Search Jobs',
        'xpath': '/html/body/footer/div/div[1]/div/nav[1]/div/div[1]/ul/li[1]/a'
    },
    {
        'title': 'Annually',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[4]/div[1]/div/div[1]/div/span'
    },
    {
        'title': 'Partner with Us',
        'xpath': '/html/body/footer/div/div[1]/div/nav[1]/div/div[2]/h3'
    },
    {
        'title': 'Summary As a Programmer Analyst C/Unix/Linux) at',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[10]/div[1]/div/div[2]'
    },
    {
        'title': '27 Sep',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[12]/div[2]'
    },
    {
        'title': 'Email Us',
        'xpath': '/html/body/footer/div/div[1]/div/nav[1]/div/div[4]/ul/li[1]/a'
    },
    {
        'title': 'Daily',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[17]/div[1]/div/div[1]/div/span'
    },
    {
        'title': 'Company',
        'xpath': '/html/body/footer/div/div[1]/div/nav[1]/div/div[3]/h3'
    },
    {
        'title': 'We are seeking a highly capable and motivated Dev',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[6]/div[1]/div/div'
    },
    {
        'title': '11 Oct',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[14]/div[2]'
    },
    {
        'title': '1',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/div[3]/ul/li[2]/a'
    },
    {
        'title': 'Annually',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[10]/div[1]/div/div[1]/div/span'
    },
    {
        'title': 'Carbon60 are currently looking for a Junior Softw',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[15]/div[1]/div/div'
    },
    {
        'title': '11 Oct',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[5]/div[2]'
    },
    {
        'title': 'Suggested Jobs',
        'xpath': '/html/body/footer/div/div[2]/ul/li[1]/a'
    },
    {
        'title': 'Annually',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[14]/div[1]/div/div[1]/div/span'
    },
    {
        'title': 'Senior Software Engineer, Fullstack Developer, C#',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[22]/div[1]/div/div'
    },
    {
        'title': ' 6 Oct',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[7]/div[2]'
    },
    {
        'title': 'Create your Profile',
        'xpath': '/html/body/nav/div/ul/li[1]/ul/li[2]/a'
    },
    {
        'title': 'Junior/Graduate Software Engineer Location: Oxfor',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[4]/div[1]/div/div[2]'
    },
    {
        'title': '11 Oct',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[17]/div[2]'
    },
    {
        'title': 'The Viator Traveller Engineering team is distribu',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[12]/div[1]/div/div'
    },
    {
        'title': ' 1 Aug',
        'xpath': '/html/body/main/div/div/div/div/div[3]/div/ul/li[1