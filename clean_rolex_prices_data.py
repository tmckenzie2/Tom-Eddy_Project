import utils as u


def main():
    table = u.read_csv('rolex_prices_data.csv')

    price_col = u.get_column(table,1)

    clean_prices = []
    for price in price_col:
        price = price.replace(',', '')
        price = price.replace('$', '')
        
        clean_prices.append(price)

    clean_table = []
    count = 0
    for row in table:
        clean_table.append([row[0], clean_prices[count]])
        count = count + 1

    u.write_to_file(clean_table, 'rolex_prices_data_clean.csv')


if __name__ == '__main__':
    main()
