import utils as u


def main():
    ebay_data = u.read_csv('ebay_data_clean.csv')
    rolex_prices_data = u.read_csv('rolex_prices_data_clean.csv')

    for e_row in ebay_data:
        for r_row in rolex_prices_data:
            r = r_row[0].split()
            if e_row[3] == r[0]:
                if int(e_row[0]) <= int(r_row[1]) + 1400:
                    e_row.append('Good deal')
                else:
                    e_row.append('Bad deal')

    for row in ebay_data:
        if len(row) == 11:
            del(row[10])

    clean_ebay_data = []
    clean_ebay_data.append(
        ['total', 'price', 'condition', 'MPN', 'movement', 'case_material', 'band_material', 'model', 'listing_type',
         'deal_type'])
    clean_ebay_data.append(
        ['total', 'price', 'condition', 'movement', 'case_material', 'band_material', 'model', 'listing_type',
         'deal_type'])
    for row in ebay_data:
        if len(row) == 10:
            clean_ebay_data.append(row)

    for row in ebay_data:
        del (row[3])


main()
