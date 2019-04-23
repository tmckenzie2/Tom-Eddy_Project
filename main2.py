from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup, SoupStrainer
from dateutil.parser import parse
import pandas as pd
import requests

# A function that requests the url, and returns the html text to be parsed by the get_details function
# The downside to requesting urls this way is that it takes a lot of time...
def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


# A function that will parse the html of the page of each item and return an attribute description
#(from the ebay ITEM SPECIFICS section) based on the attribute name input into the function
def get_details(url, att_name):
    
    att_description = "NULL"
    data = []
    table = url.find(attrs={'class':'section'})
    if table is not None:
        rows = table.findAll('tr')
        for row in rows:
            cols = row.findAll('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
    for i in data:
        if i[:1] == [att_name]:
            att_description = i[1]
        elif i[2:3] == [att_name]:
            att_description = i[3]
    
    return att_description

# Finds the raw data using ebay api and exports to excel file

# Launch Mode
'''
Keywords = input('Enter your Keywords \n')
condition = input("Condition: ")
minPrice = input("Minimum Price: ")
maxPrice = input("Maximum Price: ")
'''

# Test Mode
Keywords = "Wristwatch"
condition = "Used"
minPrice = 1000
maxPrice = 4000

# catId = input('Enter your category \n')
api = finding(appid='EddyNass-Scraper-PRD-651ca6568-7ae32d61', config_file=None)

# Data Load Prep
pageNum = 1
index = 0

# Declare data frame
global df
df = pd.DataFrame(columns=('date', 'total', 'price', 'condition', 'movement', 'case material', 'band material', 'brand', 'listingType', 'start', 'url'), dtype=float)


# Must reiterate response to update page count
response = api.execute('findCompletedItems', {
                                                'keywords': Keywords,
                                                'sortOrder': 'EndTimeLatest',
                                                'paginationInput': {'entriesPerPage': '30',
                                                                    'pageNumber': pageNum},
                                                'itemFilter': [
                                                    #{'name': 'Condition', 'value': condition},
                                                    {'name': 'SoldItemsOnly', 'value': True},
                                                    {'name': 'MinPrice', 'value': minPrice},
                                                    {'name': 'MaxPrice', 'value': maxPrice}
                                                                ]
                                            }
                       )
# Collect all items on page
soup = BeautifulSoup(response.content, 'lxml')
soup_html = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('item')

# pull prices from page
for item in items:
    price = int(round(float(item.currentprice.string)))
    dateSold = item.endtime.string
    dt = parse(dateSold)
    date = dt.date()
    url = item.viewitemurl.string.lower()
    cond = item.conditiondisplayname.string.lower()
    listingType = item.listingtype.string
    start = item.starttime.string
    dt = parse(start)
    start = dt.date()
    
    # movement, brand, case material, and band material attributes for each item
    # if the attributes are left out of the e-bay pages ITEM SPECIFICS then they will be returned as NULL
    movement = get_details(get_page(url), "Movement:")
    brand = get_details(get_page(url), "Brand:")
    case_material = get_details(get_page(url), "Case Material:")
    band_material = get_details(get_page(url), "Band Material:")
    
    try:
        shipping = int(round(float(item.shippingservicecost.string)))
        total = price + shipping
    except:
        total = price

    # push data to df
    df.loc[index] = [date, total, price, cond, movement, case_material, band_material, brand, listingType, start, url]
    index += 1
# Write to Excel. Used for Error checking, data cleaning

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df.to_excel('ebay_data.xlsx', index=False)

