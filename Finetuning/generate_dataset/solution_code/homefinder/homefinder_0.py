import csv
from lxml import etree

# Define the paths and corresponding XPaths
paths_and_xpaths = [
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[30]/a/div[1]/div[2]/div[1]', 
        'div[@class="addr-component h5 mb-0"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[4]/a/footer/div[2]', 
        'div[@class="btn btn-sm btn-primary text-nowrap"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[1]/a/footer/div[1]/div/span', 
        'span[@class="cobrand-attribution-line1 mt-1"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/header/nav/div/div[2]/div/ul[1]/li/button/span[2]', 
        'span[@class="d-lg-none d-xl-inline ml-2"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[3]/a[2]', 
        'a[@class="search-internal-link d-block"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/header/nav/div/div[2]/div/ul[2]/li[2]/a', 
        'a[@class="nav-link"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[1]/div/div[1]/h1', 
        'h1[@class="search-title"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[2]/div/p[2]', 
        'p[normalize-space()="If you decide to become a homeowner in New York, y"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[2]/div[4]/div[1]/div[2]/p', 
        'p[@class="h5 mb-0"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[2]/label', 
        'label[@class="font-weight-bold"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[1]/label', 
        'label[@class="font-weight-bold"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[2]/div/h2[2]', 
        'h2[normalize-space()="How Much Does it Cost to Buy a Home in NYC?"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[2]/div/h2[3]', 
        'h2[normalize-space()="What is NYC\'s Climate?"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[6]/a/div[1]/div[2]/div[1]', 
        'div[@class="addr-component h5 mb-0"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[13]/a/div[1]/div[1]/div', 
        'div[@class="listing-ribbon listing-ribbon-success"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[27]/a/footer/div[1]/div/span', 
        'span[@class="cobrand-attribution-line1 mt-1"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[20]/a/div[2]/div/div[1]/span', 
        'span[@class="scope-label text-homes-for-sale small"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[3]/a[10]', 
        'a[@class="search-internal-link d-block"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/footer/nav/a[3]', 
        'a[@class="order-5 order-lg-0"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[8]/div/form/div/div[1]/p[1]', 
        'p[@class="h4"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[2]/div[4]/div[3]/div[2]/p', 
        'p[@class="h5 mb-0"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[3]/label', 
        'label[@class="font-weight-bold"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[2]/div/h2[4]', 
        'h2[normalize-space()="What\'s the Best Way to Get Around in NYC?"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[1]/a/footer/div[1]/div/div/div/div', 
        'div[@class="cobrand-attribution-label"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[12]/a/footer/div[2]', 
        'div[@class="btn btn-sm btn-primary text-nowrap"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[23]/a/footer/div[1]/div/span', 
        'span[@class="cobrand-attribution-line1 mt-1"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[2]/div/div/div[1]/div/div[1]/ul/li[3]/a/span', 
        'span[normalize-space()=": 281"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[2]/a[6]', 
        'a[@class="search-internal-link d-block"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/footer/nav/a[7]', 
        'a[@class="order-2 order-lg-0"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[24]/div/div/div[1]/div/p[1]', 
        'p[@class="title h4"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[2]/div[4]/p', 
        'p[@class="h3 mb-3"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[2]/div/h2[5]', 
        'h2[normalize-space()="How Many Schools Are in NYC?"]/normalize-space()'
    ),
    (
        '/html/body/div/div/div