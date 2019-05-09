import csv
from collections import defaultdict


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


def compute_rating(col_list):
    '''
    Takes in a predicted value and an actual value and calculates the rating for those values based on the mpg info from PA2.
    This function then returns the predicted class rating and the actual rating for mpg.
    '''
    rating_list = []
    for actual_val in col_list:

        if actual_val >= 2000 and actual_val <= 2499:
            rating_list.append(1)
        elif actual_val >= 2500 and actual_val <= 2999:
            rating_list.append(2)
        elif actual_val >= 3000 and actual_val <= 3499:
            rating_list.append(3)
        elif actual_val >= 3500 and actual_val <= 3999:
            rating_list.append(4)
        elif actual_val >= 4000 and actual_val <= 4499:
            rating_list.append(5)
        elif actual_val >=4500 and actual_val <= 4999:
            rating_list.append(6)
        elif actual_val >= 5000 and actual_val <= 5499:
            rating_list.append(7)
        elif actual_val >= 5500 and actual_val <= 6999:
            rating_list.append(8)
        elif actual_val >= 7000 and actual_val <= 7499:
            rating_list.append(9)
        elif actual_val >=7500 and actual_val <= 7999:
            rating_list.append(10)
        elif actual_val >= 8000 and actual_val <= 8499:
            rating_list.append(11)
        elif actual_val >= 8500 and actual_val <= 8999:
            rating_list.append(12)
        elif actual_val >= 9000 and actual_val <= 9499:
            rating_list.append(13)
        elif actual_val >= 9500 and actual_val <= 9999:
            rating_list.append(14)
        elif actual_val >= 10000 and actual_val <= 10499:
            rating_list.append(15)
        elif actual_val >=10500 and actual_val <= 10999:
            rating_list.append(16)
        elif actual_val >= 11000 and actual_val <= 11499:
            rating_list.append(17)
        elif actual_val >= 11500 and actual_val <= 11999:
            rating_list.append(18)
        elif actual_val >= 12000 and actual_val <= 12499:
            rating_list.append(19)
        elif actual_val >= 12500 and actual_val <= 12999:
            rating_list.append(20)
        elif actual_val >= 13000 and actual_val <= 13499:
            rating_list.append(21)
        elif actual_val >=13500 and actual_val <= 13999:
            rating_list.append(22)
        elif actual_val >= 14000 and actual_val <= 14499:
            rating_list.append(23)
        elif actual_val >= 14500 and actual_val <= 14999:
            rating_list.append(24)
        elif actual_val >= 15000 and actual_val <= 15499:
            rating_list.append(25)
        elif actual_val >= 15500 and actual_val <= 15999:
            rating_list.append(26)

    return rating_list


def separateByClass(dataset,index):
    '''
    Separates a dataset into a dictionary based on the index that you specify, reads in a dataset and
    an index and returns the dictionary that is separated by the specified index values.
    '''
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if vector[index] not in separated:
            separated[vector[index]] = []
        separated[vector[index]].append(vector)
    return separated


def createProbabilityList(testInstance,totDict,priceDict,condDict,movDict,caseDict,bandDict,modDict,listDict):
    '''
    Takes in a test instance, a dictionary for the class value, dictionaries of all of the dataset attributes
    , compares certain elements at certain indexes in the test instance to the keys in the many dictionaries
    and if they are equal, the probability is appended to a new list, then the new list containing all of the
    probabilities for the test instance is returned.
    '''
    probabilityList = []
    for var in testInstance:
        for i, probability in totDict.items():
            if var[0] == i:
                
                probabilityList.append(probability)
        for i, probability in priceDict.items():
            if var[1] == i:
                
                probabilityList.append(probability)
        for i, probability in condDict.items():
            if var[2] == i:
                
                probabilityList.append(probability)
        for i, probability in movDict.items():
            if var[3] == i:
                
                probabilityList.append(probability)
        for i, probability in caseDict.items():
            if var[4] == i:
                
                probabilityList.append(probability)
        for i, probability in bandDict.items():
            if var[5] == i:
                
                probabilityList.append(probability)
        for i, probability in modDict.items():
            if var[6] == i:
                
                probabilityList.append(probability)
        for i, probability in listDict.items():
            if var[7] == i:
                
                probabilityList.append(probability)

    return probabilityList

def createDictOfProbabilities(separatedDict,separatedClass,table,index):
    '''
    Takes in a separated dictionary, a separated class dictionary, a table, and an index, compares the
    separated dictionary's class key value to check if it is equal to 'Good deal' and 'Bad deal',
    if it is, the value of a mock default dictionary is added to in order to calculate probability later on in
    the function, after all of this is done it will return a dictionary attribute probabilities.
    '''
    badDealDict = defaultdict(int)
    goodDealDict = defaultdict(int)

    for key,variables in separatedDict.items():
        for i in variables:
            if i[-1] == 'Bad deal':
                badDealDict[i[index]] += 1
            if i[-1] == 'Good deal':
                goodDealDict[i[index]] += 1
    for i in badDealDict:
        badDealDict[i] = (badDealDict[i]/len(table))/(len(separatedClass['Bad deal'])/len(table))
    for i in goodDealDict:
        goodDealDict[i] = (goodDealDict[i]/len(table))/(len(separatedClass['Good deal'])/len(table))
    
    return goodDealDict,badDealDict

def get_column(table, column_index):
    '''
    Reads in a table and an index for a column in that table, and returns that whole column as a
    float list
    '''
    column = []
    for row in table[1:]:
        if row[column_index] != "NA":
            column.append(int(row[column_index]))

    return column

def main():

    print("~~~~~~~~~~~~~~~~~~~~~~ Naive Bayes Classifier ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")

    
    col_names = ["total", "price", "condition", "movement", "case_material","band_material","model","listing_type","deal_type"]
    table = read_csv('final_training_dataset.csv')

    total_list = get_column(table,0)
    price_list = get_column(table,1)

    total_rating = compute_rating(total_list)
    price_rating = compute_rating(price_list)

    count = 0
    for row in table[1:]:
        del row[0]
        row.insert(0,(total_rating[count]))
        count = count + 1
    count = 0
    for row in table[1:]:
        del row[1]
        row.insert(1,(price_rating[count]))
        count = count + 1
        
    

    separatedDeal = separateByClass(table,-1)
    separatedListing = separateByClass(table,-2)
    separatedModel = separateByClass(table,-3)
    separatedBand = separateByClass(table,-4)
    separatedCase = separateByClass(table,-5)
    separatedMovement = separateByClass(table,-6)
    separatedCondition = separateByClass(table,-7)
    separatedPrice = separateByClass(table,-8)
    separatedTotal = separateByClass(table,-9)

    goodDealTotal,badDealTotal = createDictOfProbabilities(separatedTotal,separatedDeal,table,0)
    goodDealPrice,badDealPrice = createDictOfProbabilities(separatedPrice,separatedDeal,table,1)
    goodDealCondition,badDealCondition = createDictOfProbabilities(separatedCondition,separatedDeal,table,2)
    goodDealMovement,badDealMovement = createDictOfProbabilities(separatedMovement,separatedDeal,table,3)
    goodDealCase,badDealCase = createDictOfProbabilities(separatedCase,separatedDeal,table,4)
    goodDealBand,badDealBand = createDictOfProbabilities(separatedBand,separatedDeal,table,5)
    goodDealModel,badDealModel = createDictOfProbabilities(separatedModel,separatedDeal,table,6)
    goodDealListing,badDealListing = createDictOfProbabilities(separatedListing,separatedDeal,table,7)

    testInstance = [["8544", "8544", "pre-owned", "Automatic", "18k Gold", "Leather", "President", "FixedPrice", "????"]]

    goodDealProbabilityList = createProbabilityList(testInstance,goodDealTotal,goodDealPrice,goodDealCondition,goodDealMovement,goodDealCase,goodDealBand,goodDealModel,goodDealListing)
    badDealProbabilityList = createProbabilityList(testInstance,badDealTotal,badDealPrice,badDealCondition,badDealMovement,badDealCase,badDealBand,badDealModel,badDealListing)

    for i in testInstance:
        print("Test Instance: ",i)
    print("")

    goodDealProbabilityValue = 1
    for value in goodDealProbabilityList:
        goodDealProbabilityValue = goodDealProbabilityValue * value

    badDealProbabilityValue = 1
    for value in badDealProbabilityList:
        badDealProbabilityValue = badDealProbabilityValue * value  

    findGreatestProbDict = {}

    probabilityOfGoodDeal = goodDealProbabilityValue * (len(separatedDeal['Good deal'])/len(table))
    print("Probability of '????' being 'Good deal': ",probabilityOfGoodDeal)
    findGreatestProbDict['Good deal'] = probabilityOfGoodDeal

    probabilityOfBadDeal = badDealProbabilityValue * (len(separatedDeal['Bad deal'])/len(table))
    print("Probability of '????' being 'Bad deal': ",probabilityOfBadDeal)
    findGreatestProbDict['Bad deal'] = probabilityOfBadDeal
    
    print("")
    print("Missing class value for '????' in test case is: ",(max(findGreatestProbDict)))
    print("")
    print("")

main()



