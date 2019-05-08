from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
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
# (from the ebay ITEM SPECIFICS section) based on the attribute name input into the function we can
# utilize this to get attributes for the model, case material, band material, and movement of the
# watches. There are also other attributes that we can use
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


# Must reiterate response to update page count
def response(Keywords, pageNum, minPrice, maxPrice,api):
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
    return response


# A function to pull attributes from items
def get_attributes(items, index, df):
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
        # if the attributes are left out of the e-bay pages ITEM SPECIFICS then they
        # will be returned as NULL
        movement = get_details(get_page(url), "Movement:")
        model = get_details(get_page(url), "Model:")
        case_material = get_details(get_page(url), "Case Material:")
        band_material = get_details(get_page(url), "Band Material:")
    
        try:
            shipping = int(round(float(item.shippingservicecost.string)))
            total = price + shipping
        except:
            total = price

    # push data to df
        df.loc[index] = [date, total, price, cond, movement, case_material, band_material, model, listingType, start,
                         url]
        index += 1

    return df


# Reads in csv file and removes all rows in the file that have 'NULL' values for
# any of the attributes then saves the rows with values that do not contain 'NULL'
# to a new file
def remove_NULL_vals(file_name):
     with open('ebay_data_clean.csv', 'w', newline='') as out_file:
         with open(file_name, 'r') as my_file:
             for line in my_file:
                    columns = line.strip().split(',')
                    if all( value != 'NULL' for value in columns):
                        out_file.write(line)


def main():
    # Find the raw data using ebay api and export to excel file

    # Launch Mode
    '''
    Keywords = input('Enter your Keywords \n')
    condition = input("Condition: ")
    minPrice = input("Minimum Price: ")
    maxPrice = input("Maximum Price: ")
    '''

    # Test Mode
    Keywords = "Rolex Wristwatch"
    condition = "Used"
    minPrice = 3000
    maxPrice = 12000

    # catId = input('Enter your category \n')
    api = finding(appid='EddyNass-Scraper-PRD-651ca6568-7ae32d61', config_file=None)

    # Data Load Prep
    pageNum = 1
    index = 0

    # Declare data frame
    global df
    df = pd.DataFrame(columns=('date', 'total', 'price', 'condition', 'movement', 'case material', 'band material',
                               'model', 'listingType', 'start', 'url'), dtype=float)

    # Collect all items from ebay on page1, page2, page3, and page4 
    soup = BeautifulSoup(response(Keywords, pageNum, minPrice, maxPrice, api).content, 'lxml')
    pageNum += 1
    soup_pg_2 = BeautifulSoup(response(Keywords, pageNum, minPrice, maxPrice, api).content, 'lxml')
    pageNum += 1
    soup_pg_3 = BeautifulSoup(response(Keywords, pageNum, minPrice, maxPrice, api).content, 'lxml')
    pageNum += 1
    soup_pg_4 = BeautifulSoup(response(Keywords, pageNum, minPrice, maxPrice, api).content, 'lxml')
    items = soup.find_all('item') + soup_pg_2.find_all('item') + soup_pg_3.find_all('item') + soup_pg_4.find_all('item')

    # Call get_attributes function to get the attributes of the watches for a training set some of the attributes
    # will be NULL so we will
    # have to clean the data afterwards
    df = get_attributes(items, index, df)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Write to Excel. Used for Error checking, data cleaning
    '''
    writer = ExcelWriter('ebay_data.xlsx')
    df.to_excel(writer,'Sheet1',index=False)
    writer.save()
    '''
    # Write datafram to csv file
    df.to_csv('ebay_data.csv')

    # remove rows with NULL entries for any attributes from the training set
    remove_NULL_vals('ebay_data.csv')

    #df.to_excel('ebay_data.xlsx', index=False)

main()
