import matplotlib.pyplot as plt
import utils as u
import operator


# Set labels and capitalize first letter
def label_plt(titleLabel, xAxisLabel, yAxisLabel):
    plt.title(titleLabel.title())
    plt.ylabel(xAxisLabel.title())
    plt.xlabel(yAxisLabel.title())


# Creates a simple bar chart based on count of an attribute
def histogram(myList, attribute, filename, title, xlabel, ylabel):
    plt.figure(figsize=(20, 7))
    data = myList[1:]
    col_index = u.get_index(myList, attribute)
    x, y = u.get_frequencies(data, col_index)
    plt.bar(x, y)
    plt.title(title.title())
    plt.ylabel(xlabel.title())
    plt.xlabel(ylabel.title())
    # Save graph and close figure
    plt.savefig(filename)
    plt.close()


# Create a scatter plot with or without regression
def scatter_plot(myList, attributeX, attributeY, filename, title, xLabel, yLabel):
    plt.figure(figsize=(20, 7))
    data = myList[1:]
    x = u.get_values(data, u.get_index(myList, attributeX))
    y = u.get_values(data, u.get_index(myList, attributeY))
    plt.scatter(x, y, marker='.')
    label_plt(title, xLabel, yLabel)

    plt.savefig(filename)
    plt.close()


def main():
    table = u.read_csv('final_training_dataset.csv')
    histogram(table, 'model', 'watch-model-historgram.pdf', '5 Most Common Watch Models', 'Count', 'Model')
    scatter_plot(table, 'model', 'price', 'watch-price-scatter.pdf', 'Watch Prices', 'Model', 'Price')


if __name__ == '__main__':
    main()