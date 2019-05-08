# Description: Linear Regression
import utils as u
import numpy as np


# Get random sample
def get_random_instances(n, table):
    instances = [] * n
    for i in range(n):
        instances.append(table[np.random.randint(len(table))])

    return instances


# Takes x and y values and creates predictions
def least_squares_regression(x, y, test_values, just_stats):
    means = [np.mean(x), np.mean(y)]
    xy = 0
    xSum = 0
    ySum = 0

    for i in range(len(x)):
        xy += (x[i] - means[0]) * (y[i] - means[1])
        xSum += (x[i] - means[0]) ** 2
        ySum += (y[i] - means[1]) ** 2

    slope = xy / xSum
    intercept = means[1] - (slope * means[0])
    if just_stats is True:
        return slope, intercept

    predicted_values = []
    for x_val in test_values:
        predicted_values.append((slope * x_val) + intercept)

    return predicted_values


def preform_regression(test_num, trials):
    trial = 0
    accuracy = 0
    # Load csv into variable
    data = u.read_csv("final_training_dataset.csv")
    # Get required information and get predictions with regression
    watch_price = u.get_values(data[1:], u.get_index(data, 'price'))
    watch_deal = u.normalize_deal(u.get_values(data[1:], u.get_index(data, 'deal_type')))
    # Run Trials
    while trial <= trials:
        random_instances = get_random_instances(test_num, data[1:])  # Don't include header
        guessed_deals = least_squares_regression(watch_price, watch_deal,
                                                 u.get_values(random_instances, u.get_index(data, 'price')), False)
        guessed_deals = u.classify_deal(guessed_deals)
        # Get actual mpg values of random instances
        actual_deals = u.get_values(random_instances, u.get_index(data, 'deal_type'))

        for i in range(len(random_instances)):
            if guessed_deals[i] == actual_deals[i]:
                accuracy += 1
        trial += 1
    return accuracy


# Given a set number of test trials and set number of instances to test with each trial, how does linear regression
# using previous price as our only variable perform as a classification metric?
# Our Hypothesis: Not great
# Our Results: Supports our hypothesis, only gets around 59% accuracy
def main():
    test_num = 100
    trials = 500
    accuracy = preform_regression(test_num, trials)
    total_test = test_num * trials
    print('{:.2f}%'.format(accuracy/total_test), 'overall accuracy with linear regression using', trials, 'trials')


if __name__ == '__main__':
    main()