from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
from dateutil.parser import parse
import pandas as pd

# Finds the raw data using ebay api and exports to excel file

# Launch Mode
'''
Keywords = input('Enter your Keywords \n')
condition = input("Condition: ")
minPrice = input("Minimum Price: ")
maxPrice = input("Maximum Price: ")
'''

# Test Mode
Keywords = "Omega Speedmaster"
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
df = pd.DataFrame(columns=('date', 'total', 'price', 'condition', 'listingType', 'start', 'url'), dtype=float)


# Must reiterate response to update page count
response = api.execute('findCompletedItems', {
                                                'keywords': Keywords,
                                                'sortOrder': 'EndTimeLatest',
                                                'paginationInput': {'entriesPerPage': '100',
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

    try:
        shipping = int(round(float(item.shippingservicecost.string)))
        total = price + shipping
    except:
        total = price

    # push data to df
    df.loc[index] = [date, total, price, cond, listingType, start, url]
    index += 1
'''
# Write to Excel. Used for Error checking, data cleaning
df.to_excel('ebay_data.xlsx', index=False)
'''
