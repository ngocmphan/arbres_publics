import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bokeh.io import output_file, show
from bokeh.plotting import figure

trees = pd.read_csv("arbres-publics.csv", dtype={'ARROND_NOM': str, 'Rue': str}, low_memory=False)

print(trees.info())
print(trees['COTE'].unique())
print(trees['COTE'].value_counts())
print(trees['ESSENCE_ANG'].value_counts())
print(trees['ESSENCE_ANG'].unique())


