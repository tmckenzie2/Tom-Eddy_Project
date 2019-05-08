import csv


# Reads in a 2d list and a string that you would like to save a file as
# and writes that 2d list to the file named after save_file_as
def write_to_file(table_name,save_file_as):
    with open(save_file_as, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(table_name)

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


def main():
    ebay_data = read_csv('ebay_data_clean.csv')
    rolex_prices_data = read_csv('rolex_prices_data_clean.csv')

    for e_row in ebay_data:
        for r_row in rolex_prices_data:
            r = r_row[0].split()
            if e_row[3] == r[0]:
                if int(e_row[0]) <= int(r_row[1]) + 1400:
                    e_row.append('Good deal')
                else:
                    e_row.append('Bad deal')

    for row in ebay_data:
        if (len(row) == 11):
            del(row[10])
    clean_ebay_data = []
    clean_ebay_data.append(['total', 'price', 'condition', 'MPN', 'movement', 'case_material', 'band_material', 'model',
                            'listing_type', 'deal_type'])
    for row in ebay_data:
        if (len(row) == 10):
            clean_ebay_data.append(row)
    write_to_file(clean_ebay_data, 'final_training_dataset.csv')


main()
