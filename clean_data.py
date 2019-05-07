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



def remove_modelnums_not_applicable(file_name):
     with open('ebay_data_clean.csv', 'w', newline='') as out_file:
         with open(file_name, 'r') as my_file:
             for line in my_file:
                    columns = line.strip().split(',')
                    if all( value.lower() != 'does not apply' for value in columns):
                        out_file.write(line)



def main():
    table = read_csv('ebay_data_dirty.csv')
    print(table)

    for row in table:
        del row[0]
        del row[0]
        del row[9]
        del row[-1]

    write_to_file(table,'ebay_data_dirty_temp.csv')
        

    remove_modelnums_not_applicable('ebay_data_dirty_temp.csv')

    

main()
    
