import csv
import itertools


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


def read_csv(filename):
    '''
    Reads in a csv file and returns a table as a list of lists (rows)
    '''
    the_file = open(filename, 'r')
    the_reader = csv.reader(the_file, dialect='excel')
    table = []
    for row in the_reader:
        if len(row) > 0:
            table.append(row)
    the_file.close()
    return table


def apriori_prune_C1(table,Ck,minsup):
    '''
    takes in a more complex dataset of only one value each, a set of unique attributes Ck and a minsup and removes every
    attribute that is below the minsup for designated minsup
    '''
    L = []
    for c in Ck:
        i = c.split('=')
        tempL = []
        tempL.append(i[1])
        if compute_frequency(table,set(tempL)) >= minsup:
            L.append(c)
    return sorted(L)


def compute_subsets(s):
    '''
    takes in a list and returns all subsets of that list
    '''
    # Base case
    if len(s) == 0:
        return [[]]
    # The input set is not empty, divide and conquer!
    h, t = s[0], s[1:]
    ss_excl_h = compute_subsets(t)
    ss_incl_h = [([h] + ss) for ss in ss_excl_h]
    subsets = ss_incl_h + ss_excl_h
    return subsets


def apriori_prune(table,Ck,minsup):
    '''
    takes in a more complex dataset, a set of unique attributes Ck and a minsup and removes every
    attribute that is below the minsup for designated minsup
    '''
    L = []
    for c in Ck:
        temp = []
        for i in c:
            x = str(i).split('=')
            temp.append(x[1])
            
        if compute_frequency(table,set(temp)) >= minsup:
            L.append(c)
    return sorted(L)


def apriori_gen(itemsets, length):
    """Generates candidate k-itemsets."""
    return itertools.combinations(itemsets, length)


def apriori(header,table, minsup, minconf):
    '''
    Function that mimics an apriori algorithm, takes in a header of class attributes, a dataset,
    a minimum support and minimum confidence and returns the rules that are evaluated by the
    algorithm
    '''
    supported_itemsets = []
    final_itemsets = []
    # implement apriori here
    # call your compute_unique_values() to get I
    I = compute_unique_values(header,table)
    L1 = apriori_prune_C1(table,I,minsup)
    k = 2
    supported_itemsets = apriori_gen(L1,k)
    supported_itemsets = apriori_prune(table,supported_itemsets,minsup)
    for itemset in supported_itemsets:
        final_itemsets.append(itemset)
    k += 1
    while supported_itemsets != []:
        supported_itemsets = apriori_gen(set([ item for innerlist in supported_itemsets for item in innerlist ]),k)
        supported_itemsets = apriori_prune(table,supported_itemsets,minsup)
        for itemset in supported_itemsets:
            check = apriori_prune(table,supported_itemsets,minsup)
            if apriori_gen(set([ item for innerlist in check for item in innerlist ]),k+1) != []:
                final_itemsets.append(itemset)
        k += 1
        
    final_no_dups = []
    for row in final_itemsets:
        split = []
        append_yes = 0
        for i in row:
            i = str(i).split("=")
            split.append(i[0])
        for a, b in itertools.combinations(split, 2):
            if a == b:
                append_yes = 1
        if append_yes == 0:
            final_no_dups.append(row)

    rules = generate_apriori_rules(table, final_no_dups, minconf)
    return rules


def generate_apriori_rules(table, supported_itemsets, minconf):
    '''
    A function that takes in a more complex dataset, a list of supported itemsets for the dataset and a minimum confidence
    level and generates rules based on all of these.
    '''
    rules = []
   
    for S in supported_itemsets:
        possible_subsets = compute_subsets(list(set(S)))
        for subset in possible_subsets[1:-1]:
            LHS = subset
            RHS = [item for item in S if item not in LHS]
            split_LuR = []
            for i in S:
                x = str(i).split("=")
                split_LuR.append(x[1])
            countLuR = frequency(table,set(split_LuR))
            split_L = []
            for i2 in LHS:
                x2 = str(i2).split("=")
                split_L.append(x2[1])
            countL = frequency(table,set(split_L))
            split_R = []
            for i3 in RHS:
                x3 = str(i3).split("=")
                split_R.append(x3[1])
            countR = frequency(table,set(split_R))
            conf = countLuR/countL
            support = countLuR/len(table)
            lift = countLuR/(countL * countR)
            if conf >= minconf:
                rules.append(str(LHS) + " -> " + str(RHS) + ", Confidence: " + str(conf) + ", Support: " + str(support)
                             + ", Lift: " + str(lift))
    return rules


def compute_unique_values(header,table):
    '''
    A function that takes a header and a table and computes the unique attributes in that
    table
    '''
    unique_values = set()
    
    for row in table:
        i = 0
        for value in row:
            unique_values.add(str(header[i]) + "=" + str(value))
            i += 1
    return sorted(list(unique_values))


def frequency(table,item):
    '''
    a slightly modified function that computes the frequency of a specific item occuring in a table
    '''
    item_count = 0
    for row in table:
        if item.issubset(row):
            item_count += 1
    return item_count


def compute_frequency(table,item):
    '''
    computes the frequency of a specific item occuring in a table
    '''
    item_count = 0
    for row in table:
        if item.issubset(row):
            item_count += 1
    item_count = item_count/len(table)
    return item_count


def main():
    # Replace header with header for watch dataset
    header = ["total", "price", "condition", "MPN", "movement","case_material","band_material","model","listing_type","deal_type"]

    # Read csv of clean ebay data in and assign it to a variable
    watch_dataset = read_csv("final_training_dataset.csv")
    
    watch_rules = apriori(header,watch_dataset,0.35,0.80)
    for rules in watch_rules:
        print(rules)


main()
