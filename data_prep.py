import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bokeh.io import output_file, show
from bokeh.plotting import figure

trees = pd.read_csv("arbres-publics.csv", dtype={'ARROND_NOM': str, 'Rue': str}, low_memory=False)
trees['count'] = 1

print(trees.info())
print(trees['COTE'].unique())

cote_count = pd.pivot_table(trees, values='count', index='COTE', aggfunc=np.sum)
print(cote_count)

p = figure(plot_height=250, title="Side count",
           toolbar_location=None, tools="")

p.vbar(x=cote_count.index, top=cote_count['count'], width=0.9)

show(p)