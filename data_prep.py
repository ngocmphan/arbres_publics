import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bokeh.io import output_file, show
from bokeh.plotting import figure
from pyproj import Proj, transform, Transformer
from functools import partial


def place_col(df):
    df['place'] = np.where(df['Emplacement'].str.contains('parterre'), 'parterre',
                np.where(df['Emplacement'].str.contains('banquette'), 'banquette',
                np.where(df['Emplacement'].str.contains('terre-plein'), 'terre-plein',
                np.where(df['Emplacement'].str.contains('trottoir'), 'trottoir',
                np.where(df['Emplacement'].str.contains('parc'), 'parc',
                np.where(df['Emplacement'].str.contains('saillie'), 'saillie',
                np.where(df['Emplacement'].str.contains('verdure'), 'îlot de verdure', 'others')
                                                                        ))))))
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
print(trees[['Coord_X', 'Coord_Y', 'Longitude', 'Latitude']].head(5))

# Quebec MTM : epsg 2950. Proj: convert lon, lat -> x,y coords. Inverse. Utm 18



