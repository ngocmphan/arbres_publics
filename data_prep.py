import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bokeh.io import output_file, show
from bokeh.plotting import figure

trees = pd.read_csv("arbres-publics.csv", dtype={'ARROND_NOM': str, 'Rue': str}, low_memory=False)

# Missing values handling
trees['DHP'] = trees['DHP'].fillna((trees['DHP'].mean()))
# print(trees.info())


# Variable transformation
trees['Emplacement'] = trees['Emplacement'].str.lower()


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


trees_new = place_col(trees)

print(trees_new['place'].value_counts())

