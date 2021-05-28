import pandas as pd
import numpy as np


def place_col(df):
    """ Return data frame with a new column called 'place'
    including 8 categories of original 30 categories 'Emplacement' variable """
    def string_test(row):
        if 'parterre' in row:
            return 'parterre'
        elif 'banquette' in row:
            return 'banquette'
        elif 'terre-plein' in row:
            return 'terre-plein'
        elif 'trottoir' in row:
            return 'trottoir'
        elif 'parc' in row:
            return 'parc'
        elif 'saillie' in row:
            return 'saillie'
        elif 'verdure' in row:
            return 'îlot de verdure'
        else:
            return 'others'

    df['place'] = df.apply(lambda x: string_test(x['Emplacement']), axis=1)

    return df


trees = pd.read_csv("arbres-publics.csv", dtype={'ARROND_NOM': str, 'Rue': str}, low_memory=False)

# Missing values handling
trees['DHP'] = trees['DHP'].fillna((trees['DHP'].mean()))

# Variable transformation
trees['Emplacement'] = trees['Emplacement'].str.lower()
trees_new = place_col(trees)

# Questions

# 1 Comparison between on-road and off-road trees:
no_on_off_road = trees_new['INV_TYPE'].value_counts()

# 2 Top 3 areas with most trees
areas = trees_new['ARROND_NOM'].value_counts()

# 3 Top 3 most planted trees
trees_type = trees_new['ESSENCE_ANG'].value_counts()

# 4 Type of earth where trees are most planted
earth_type = trees_new['place'].value_counts()
print(earth_type)
print(trees_new.info())




