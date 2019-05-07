import csv

#Reads in a 2d list and a string that you would like to save a file as
#and writes that 2d list to the file named after save_file_as
def write_to_file(table_name,save_file_as):
    with open(save_file_as, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(table_name)
        
#Reads in a csv file and returns a table as a list of lists (rows)
def read_csv(filename):
    the_file = open(filename, 'r')
    the_reader = csv.reader(the_file, dialect='excel')
    table = []
    for row in the_reader:
        if len(row) > 0:
            table.append(row)
    the_file.close()
    return table


def get_column(table, column_index):
    '''
    Reads in a table and an index for a column in that table, and returns that whole column as a
    list.
    '''
    column = []
    for row in table:
        if row[column_index] != "NA":
            column.append(row[column_index])

    return column

def main():
    table = read_csv('rolex_prices_data.csv')

    price_col = get_column(table,1)

    clean_prices = []
    for price in price_col:
        price = price.replace(',','')
        price = price.replace('$','')
        
        clean_prices.append(price)

    clean_table = []
    count = 0
    for row in table:
        clean_table.append([row[0],clean_prices[count]])
        count = count +1

    write_to_file(clean_table,'rolex_prices_data_clean.csv')   

main()
    
