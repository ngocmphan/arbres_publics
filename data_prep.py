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

print(trees_new.info())



