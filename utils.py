import csv


# Reads in a csv file and returns a table as a list of lists (rows)
def read_csv(filename):
    the_file = open(filename, 'r')
    the_reader = csv.reader(the_file, dialect='excel')
    table = []
    for row in the_reader:
        if len(row) > 0:
            table.append(row)
    the_file.close()
    return table


# Reads in a 2d list and a string that you would like to save a file as
# and writes that 2d list to the file named after save_file_as
def write_to_file(table_name,save_file_as):
    with open(save_file_as, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(table_name)


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


# Get values for certain column index and force float type
def get_values(table, column_index):
    values = []
    for row in table:
        try:
            values.append(float(row[column_index]))
        except:
            values.append(row[column_index])
    return values


# Given column name, return integer index
def get_index(myList, attribute):
    headers = myList[0]
    for i in range(len(headers)):
        if headers[i] == attribute:
            index = i

    return index