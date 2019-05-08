# Description: Use random classifier and Zero-R classifiers to dispel common financial myths.
# Myth 1: Price is impossible to predict and moves in a "Random walk", meaning it will randomly go up or down.
# Myth 2: Past results indicate future results. If the last few watches to sell were a good deal, this one MUST
# be a good deal, right?
import utils as u
from numpy.random import choice


# Use probabilities of data set to randomly select classes
def random_classifier():
    data = u.read_csv("final_training_dataset.csv")
    class_labels = {'Good deal': 0, 'Bad deal': 0}
    # Count Good deal' and Bad deal's
    for row in data[1:]:
        if row[-1] == 'Good deal':
            class_labels['Good deal'] += 1
        else:
            class_labels['Bad deal'] += 1
    # Calculate probability
    chance_good = class_labels['Good deal'] / len(data[1:])
    chance_bad = class_labels['Bad deal'] / len(data[1:])

    # Get random choices based on probability. We will collect as many random numbers as we have rows in the table
    choices = choice(['Good Deal', 'Bad deal'], len(data[1:]), p=[chance_good, chance_bad])
    accuracy = 0
    i = 1
    # Check accuracy
    for classifier in choices:
        if classifier == data[i][-1]:
            accuracy += 1
        i += 1
    accuracy = accuracy / len(data[1:])
    print(
        "===========================================\n "
        "Random Choice Classifier\n"
        "===========================================")
    print("Accuracy = {}, error rate = {}".format(round(accuracy, 2), round(1-accuracy, 2)))


# Zero_R classification method of prediction
def zero_r():
    data = u.read_csv("final_training_dataset.csv")
    class_labels = {'Good deal': 0, 'Bad deal': 0}
    # Count Good deal' and Bad deal's
    for row in data[1:]:
        if row[-1] == 'Good deal':
            class_labels['Good deal'] += 1
        else:
            class_labels['Bad deal'] += 1

    # Calculate probability
    chance_good = class_labels['Good deal'] / len(data[1:])
    chance_bad = class_labels['Bad deal'] / len(data[1:])

    # Get higher probability
    if chance_good > chance_bad:
        choice = 'Good deal'
    else:
        choice = 'Bad deal'

    accuracy = 0
    i = 1
    for row in data:
        if row[-1] == choice:
            accuracy += 1
        i += 1
    accuracy = accuracy / len(data[1:])
    print(
        "\n===========================================\n "
        "Zero-R Classifier\n"
        "===========================================")
    print("Accuracy = {}, error rate = {}".format(round(accuracy, 2), round(1-accuracy, 2)))


# Run all the steps
def main():
    random_classifier()
    zero_r()


if __name__ == '__main__':
    main()
