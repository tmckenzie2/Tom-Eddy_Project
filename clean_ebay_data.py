import utils as u


def clean_watch_model(model_col):
    clean_model_col = []
    for i in model_col:
        if "oysterdate".casefold() in i.casefold():
            clean_model_col.append('Oysterdate')
        elif "Datejust 2".casefold() in i:
            clean_model_col.append('Datejust 2')
        elif "Datejust II".casefold() in i:
            clean_model_col.append('Datejust 2')
        elif "just".casefold() in i.casefold():
            clean_model_col.append('Datejust')
        elif "Explorer II" in i:
            clean_model_col.append('Explorer 2')
        elif "Explorer 2".casefold() in i.casefold():
            clean_model_col.append('Explorer 2')
        elif "Explorer".casefold() in i.casefold():
            clean_model_col.append('Explorer')
        elif "Yacht".casefold() in i.casefold():
            clean_model_col.append('Yachmaster')
        elif "midas".casefold() in i.casefold():
            clean_model_col.append('King Midas')
        elif "Air".casefold() in i.casefold():
            clean_model_col.append('Air-King')
        elif "Cellini".casefold() in i.casefold():
            clean_model_col.append('Cellini')
        elif "daytona".casefold() in i.casefold():
            clean_model_col.append('Daytona')
        elif "mast II".casefold() in i.casefold():
            clean_model_col.append('GMT-Master 2')
        elif "Master II".casefold() in i:
            clean_model_col.append('GMT-Master 2')
        elif "milgaus".casefold() in i.casefold():
            clean_model_col.append('Milgauss')
        elif "perpetual".casefold() in i.casefold():
            clean_model_col.append('Oysterdate')
        elif "master".casefold() in i.casefold():
            clean_model_col.append('GMT-Master')
        elif "milgaus".casefold() in i.casefold():
            clean_model_col.append('Milgauss')
        elif "pilot".casefold() in i.casefold():
            clean_model_col.append('Pilot')
        elif "president".casefold() in i.casefold():
            clean_model_col.append('President')
        elif "deepsea".casefold() in i.casefold():
            clean_model_col.append('Sea-Dweller')
        elif "dweller".casefold() in i.casefold():
            clean_model_col.append('Sea-Dweller')
        elif "precision".casefold() in i.casefold():
            clean_model_col.append('Oysterdate')
        elif "oyster".casefold() in i.casefold():
            clean_model_col.append('Oysterdate')
        elif "turn-o".casefold() in i.casefold():
            clean_model_col.append('Turn-O-Graph')
        elif "submarine".casefold() in i.casefold():
            clean_model_col.append('Submariner')
        elif "turn-o".casefold() in i.casefold():
            clean_model_col.append('Turn-O-Graph')
        elif "vintage".casefold() in i.casefold():
            clean_model_col.append('Vintage')
        elif "date".casefold() in i.casefold():
            clean_model_col.append('Datejust')
        else:
            clean_model_col.append(i)
    return clean_model_col


def clean_case_material(case_col):

    clean_case_col = []
    for i in case_col:
        if "plati".casefold() in i.casefold():
            clean_case_col.append('Platinum')
        elif "14".casefold() in i.casefold():
            clean_case_col.append('14k Gold')
        elif "18" in i.casefold():
            clean_case_col.append('18k Gold')
        elif "gold".casefold() in i.casefold():
            clean_case_col.append('18k Gold')
        elif "silv".casefold() in i.casefold():
            clean_case_col.append('Silver')
        elif "stain".casefold() in i.casefold():
            clean_case_col.append('Stainless Steel')
        elif "steel".casefold() in i.casefold():
            clean_case_col.append('Stainless Steel')
        else:
            clean_case_col.append(i)
    return clean_case_col


def clean_band_material(band_col):
    clean_band_col = []
    for i in band_col:
        if "& 10k".casefold() in i.casefold():
            clean_band_col.append('Two Tone 10k Gold')
        elif "& 14k".casefold() in i.casefold():
            clean_band_col.append('Two Tone 14k Gold')
        elif "and" in i.casefold():
            clean_band_col.append('Two Tone 18k Gold')
        elif "&" in i.casefold():
            clean_band_col.append('Two Tone 18k Gold')
        elif "Croco".casefold() in i.casefold():
            clean_band_col.append('Crocodile')
        elif "alliga".casefold() in i.casefold():
            clean_band_col.append('Alligator')
        elif "ceram" in i.casefold():
            clean_band_col.append('Ceramic')
        elif "leath" in i.casefold():
            clean_band_col.append('Leather')
        elif "plati".casefold() in i.casefold():
            clean_band_col.append('Platinum')
        elif "14".casefold() in i.casefold():
            clean_band_col.append('14k Gold')
        elif "18" in i.casefold():
            clean_band_col.append('18k Gold')
        elif "gold".casefold() in i.casefold():
            clean_band_col.append('18k Gold')
        elif "stain".casefold() in i.casefold():
            clean_band_col.append('Stainless Steel')
        elif "steel".casefold() in i.casefold():
            clean_band_col.append('Stainless Steel')
        elif "oyster".casefold() in i.casefold():
            clean_band_col.append('Stainless Steel')
        elif "rubber".casefold() in i.casefold():
            clean_band_col.append('Rubber')
        else:
            clean_band_col.append(i)
    return (clean_band_col)


def clean_watch_movement(movement_col):
    clean_movement_col = []
    for i in movement_col:
        if "Quar".casefold() in i.casefold():
            clean_movement_col.append('Quartz')
        elif "3035".casefold() in i.casefold():
            clean_movement_col.append('Automatic')
        elif "manual".casefold() in i.casefold():
            clean_movement_col.append('Manual')
        elif "auto".casefold() in i.casefold():
            clean_movement_col.append('Automatic')
        elif "mechan".casefold() in i.casefold():
            clean_movement_col.append('Automatic')
        
        
        else:
            clean_movement_col.append(i)

    return clean_movement_col


def remove_modelnums_not_applicable(file_name):
    with open('ebay_data_clean.csv', 'w', newline='') as out_file:
        with open(file_name, 'r') as my_file:
            for line in my_file:
                    columns = line.strip().split(',')
                    if all(value.lower() != 'does not apply' for value in columns):
                        out_file.write(line)


def main():
    table = u.read_csv('ebay_data_dirty.csv')

    for row in table:
        del row[0]
        del row[0]
        del row[9]
        del row[-1]

    u.write_to_file(table, 'ebay_data_dirty_temp.csv')
    remove_modelnums_not_applicable('ebay_data_dirty_temp.csv')
    table_w_modelnums = u.read_csv('ebay_data_clean.csv')

    case_col = u.get_column(table_w_modelnums, 5)
    clean_case = clean_case_material(case_col)

    count = 0
    for row in table_w_modelnums:
        del row[5]
        row.insert(5,str(clean_case[count]))
        count = count + 1

    movement_col = u.get_column(table_w_modelnums, 4)
    clean_movement = clean_watch_movement(movement_col)

    count = 0
    for row in table_w_modelnums:
        del row[4]
        row.insert(4,str(clean_movement[count]))
        count = count + 1

    band_col = u.get_column(table_w_modelnums, 6)
    clean_band = clean_band_material(band_col)

    count = 0
    for row in table_w_modelnums:
        del row[6]
        row.insert(6,str(clean_band[count]))
        count = count + 1

    mod_col = u.get_column(table_w_modelnums, 7)
    clean_mod = clean_watch_model(mod_col)

    count = 0
    for row in table_w_modelnums:
        del row[7]
        row.insert(7,str(clean_mod[count]))
        count = count + 1
    u.write_to_file(table_w_modelnums, "ebay_data_clean.csv")


if __name__ == '__main__':
    main()
