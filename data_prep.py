import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bokeh.io import output_file, show
from bokeh.plotting import figure
from pyproj import Proj, transform, Transformer
from functools import partial


def place_col(df):
    place = ['parterre', 'banquette', 'terre-plein',
             'trottoir', 'parc', 'saillie', 'verdure']
    for p in place:
        for i, row in df.iterrows():
            if p in row['Emplacement']:
                row['place'] = p
            else:
                row['place'] = 'others'

    # df['place'] = np.where(
    #     df['Emplacement'].str.contains('parterre'), 'parterre',
    #     np.where(df['Emplacement'].str.contains('banquette'), 'banquette',
    #              np.where(df['Emplacement'].str.contains('terre-plein'), 'terre-plein',
    #                       np.where(df['Emplacement'].str.contains('trottoir'), 'trottoir',
    #                                np.where(df['Emplacement'].str.contains('parc'), 'parc',
    #                                         np.where(df['Emplacement'].str.contains('saillie'), 'saillie',
    #                                                  np.where(df['Emplacement'].str.contains('verdure'), 'îlot de verdure', 'others')

    # ))))))
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

print(trees_new['place'].value_counts())

print(trees.info())





