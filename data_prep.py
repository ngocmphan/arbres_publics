import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bokeh.io import output_file, show
from bokeh.plotting import figure
from pyproj import Proj, transform, Transformer
from functools import partial


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


def xy_to_lonlat(x, y):
    p = Proj(proj='utm', zone=19, ellps='WGS84', preserve_units=False)
    lonlat = p(x, y, inverse=True)
    return lonlat[0], lonlat[1]


trees = pd.read_csv("arbres-publics.csv", dtype={'ARROND_NOM': str, 'Rue': str}, low_memory=False)

# Missing values handling
trees['DHP'] = trees['DHP'].fillna((trees['DHP'].mean()))

# Variable transformation
trees['Emplacement'] = trees['Emplacement'].str.lower()
trees_new = place_col(trees)

print(trees.info())






