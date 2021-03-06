from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
from dateutil.parser import parse
import pandas as pd
import requests
import csv

'''
Important Note: run this code to calculate a training set of 100 items per execution
In order to get a dataset of 1000 items, run the code 10 times and make sure to increment the integer 
value of 1 in the line of code: soup = BeautifulSoup(response(Keywords, 1, minPrice, maxPrice, api).content, 'lxml')
in main() each time you run it. You will also need to save the data to a separate csv file each time you execute,
this means that in the line of code df.to_csv('ebay_data1.csv') and remove_NULL_vals('ebay_data1.csv')
in main(), you need to change the file each time you run the code so that the file run in the previous
execution is not overwritten and also change the file in the line of code: with open('ebay_data_dirty1.csv', 'w', newline='') as out_file:
in the function remove_NULL_vals so that that file is also not overwritten.
'''


# A function that requests the url, and returns the html text to be parsed by the get_details function
# The downside to requesting urls this way is that it takes a lot of time...
def get_page(url):
    response = requests.get(url, headers={'Connection': 'close'})
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


# A function that will parse the html text of the page bobswatches.com/used-rolex-prices and return a table
# of rolex models and their cooresponding classification so that we can classify the rolexes on ebay as a good
# or a bad deal
def get_prices_db(url):
    data = []
    table = url.find(attrs={'class': 'watchPriceTable tablesorter'})
    if table is not None:
        rows = table.findAll('tr')
        for row in rows:
            cols = row.findAll('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
    return data


# A function that will parse the html of the page of each item and return an attribute description
# (from the ebay ITEM SPECIFICS section) based on the attribute name input into the function we can
# utilize this to get attributes for the model, case material, band material, and movement of the
# watches. There are also other attributes that we can use
def get_details(url, att_name):
    att_description = "NULL"
    data = []
    table = url.find(attrs={'class': 'section'})
    print(table)
    quit()
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
def response(Keywords, pageNum, minPrice, maxPrice, api):
    response = api.execute('findCompletedItems', {
        'keywords': Keywords,
        'sortOrder': 'EndTimeLatest',
        'paginationInput': {'entriesPerPage': '100',
                            'pageNumber': pageNum},
        'itemFilter': [
            # {'name': 'Condition', 'value': condition},
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

        MPN = get_details(get_page(url), "MPN:")
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
        df.loc[index] = [date, total, price, cond, MPN, movement, case_material, band_material, model, listingType,
                         start, url]
        index += 1

    return df


# Reads in csv file and removes all rows in the file that have 'NULL' values for
# any of the attributes then saves the rows with values that do not contain 'NULL'
# to a new file
def remove_NULL_vals(file_name):
    with open('ebay_data_dirty1.csv', 'w', newline='') as out_file:
        with open(file_name, 'r') as my_file:
            for line in my_file:
                columns = line.strip().split(',')
                if all(value != 'NULL' for value in columns):
                    out_file.write(line)


# Reads in a table and an index for a column in that table, and returns that whole column as a
# list
def get_column(table, column_index):
    column = []
    for row in table:
        if row[column_index] != "NA":
            column.append(row[column_index])

    return column


# Reads in a 2d list and a string that you would like to save a file as
# and writes that 2d list to the file named after save_file_as
def write_to_file(table_name, save_file_as):
    with open(save_file_as, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(table_name)


def main():
    # Find the raw data using ebay api and export to excel file
    api = finding(appid='EddyNass-Scraper-PRD-651ca6568-7ae32d61', config_file=None)

    # Data Load Prep
    index = 0

    # Declare data frame
    df = pd.DataFrame(columns=('date', 'total', 'price', 'condition', 'MPN', 'movement', 'case material',
                               'band material', 'model', 'listingType', 'start', 'url'), dtype=float)

    # Run this to collect data from the ebay website with BeatifulSoup
    # This code will return 100 results per page
    Keywords = "Rolex Wristwatch"
    minPrice = 3000
    maxPrice = 12000
    pageNum = 1
    # Collect all items from ebay on page1 through 4
    while pageNum <= 4:
        soup = BeautifulSoup(response(Keywords, pageNum, minPrice, maxPrice, api).content, 'lxml')
        if pageNum == 1:
            items = soup.find_all('item')
        else:
            items += soup.find_all('item')
        pageNum += 1

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
    df.to_csv('ebay_data1.csv')

    # remove rows with NULL entries for any attributes from the training set
    remove_NULL_vals('ebay_data1.csv')

    rolex_prices_data = get_prices_db(get_page('https://www.bobswatches.com/used-rolex-prices'))
    model_num = get_column(rolex_prices_data[1:], 0)
    market_price = get_column(rolex_prices_data[1:], -1)

    market_price_data = []

    for i in model_num:
        market_price_data.append([i])
    count = 0
    for row in market_price_data:
        row.insert(1, market_price[count])
        count = count + 1

    write_to_file(market_price_data, 'rolex_prices_data.csv')


main()
