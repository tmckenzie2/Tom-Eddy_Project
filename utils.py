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


# Assign 1 to good deal, 0 to bad deal
def normalize_deal(data):
    new_data = []
    for deal in data:
        if deal == 'Good deal':
            new_data.append(1)
        else:
            new_data.append(0)
    return new_data


# Assign good deal if prediction is at or above .5
def classify_deal(data):
    classify = []
    for num in data:
        if num >= .5:
            classify.append('Good deal')
        else:
            classify.append('Bad deal')
    return classify


def replace_deal(table):
    for row in table:
        if row[-1] == 'Good deal':
            row[-1] = 1
        else:
            row[-1] = 0


def get_frequencies(table, column_index):
    column = sorted(get_column(table, column_index))
    values = []
    counts = []

    for value in column:
        if value not in values:
            values.append(value)
            # first time we have seen this value
            counts.append(1)
        else:  # we've seen it before, the list is sorted...
            counts[-1] += 1

    return values, counts
