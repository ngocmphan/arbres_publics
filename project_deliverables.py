from data_prep import trees_new
import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler
import mca

# Questions

# 1 Comparison between on-road and off-road trees:
no_on_off_road = trees_new['INV_TYPE'].value_counts()

# 2 Top 3 areas with most trees
areas = trees_new['ARROND_NOM'].value_counts()

# 3 Top 3 most planted trees
trees_type = trees_new['ESSENCE_ANG'].value_counts()
top_10_trees = list(trees_type[:10].index)

# 4 Type of earth where trees are most planted
earth_type = trees_new['place'].value_counts()

# 6 Compare the DHP of trees in different areas
box_plot = trees_new.boxplot(column=['DHP'], by=['ARROND_NOM'], fontsize=8)
ax = sns.boxplot(x='ARROND_NOM', y='DHP', data=trees_new)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.close()

histo = sns.displot(trees_new, x='DHP', hue='ARROND_NOM', kind='kde',
                    fill=True,
                    height=5, aspect=5)
plt.close()

# 5 95% Confidence interval for DHP of trees.
std = trees_new['DHP'].std()
mean = trees_new['DHP'].mean()
n = trees_new['DHP'].count()
multiplier = std/sqrt(n)
fig, ax = plt.subplots()
sns.histplot(trees_new, x='DHP').set_title('Distribution plot of trees diameter')
ax.set_xlim(0, 120)
plt.close()
CI_mtl = 'Confidence interval of Montreal trees: [{0:2f}, {1:2f}]'\
    .format(mean-1.96*multiplier, mean+1.96*multiplier)

# 6 DHP measure of the trees on road and off road
on_road = trees_new.loc[trees_new['INV_TYPE'] == 'R']
off_road = trees_new.loc[trees_new['INV_TYPE'] == 'H']

on_road_place = on_road['Emplacement'].value_counts()
off_road_place = off_road['Emplacement'].value_counts()

fig, ax = plt.subplots()
on_road_plot = sns.histplot(on_road, x='DHP', label='on_road', color='red')
off_road_plot = sns.histplot(off_road, x='DHP', label='off_road', color='blue')
ax.set_xlim(0, 120)
plt.title('Distribution plot of on and off road trees')
plt.legend()
plt.close()

box_plot_on_off = sns.boxplot(x='INV_TYPE', y='DHP', data=trees_new)
plt.title('Box plot of on and off road trees')
plt.close()

std_on_road = on_road['DHP'].std()
std_off_road = off_road['DHP'].std()

mean_on_road = on_road['DHP'].mean()
mean_off_road = off_road['DHP'].mean()

n_on_road = on_road['DHP'].count()
n_off_road = off_road['DHP'].count()

multiplier_on_road = std/sqrt(n_on_road)
multiplier_off_road = std/sqrt(n_off_road)

CI_mtl_road = 'Confidence interval of on road trees: [{0:2f}, {1:2f}]'.\
    format(mean_on_road - 1.96*multiplier_on_road,
           mean_on_road + 1.96*multiplier_on_road)
CI_mtl_off_road = 'Confidence interval of off road trees: [{0:2f}, {1:2f}]'\
    .format(mean_off_road - 1.96*multiplier_off_road,
            mean_off_road + 1.96*multiplier_off_road)

# 7 Profile the placement of the trees
box_plot_place = sns.boxplot(x='place', y='DHP', data=trees_new)
plt.title('Box plot of different trees placements')
plt.close()

# 8 Clustering to identify group of trees
cluster_df = trees_new[['INV_TYPE', 'place', 'DHP', 'ARROND_NOM', 'ESSENCE_ANG']]
cluster_df = cluster_df[cluster_df['ESSENCE_ANG'].isin(top_10_trees)]


def cluster_processing(df):
    """ Processing data frame for cluster kmean: trees_type, place, trees
    name, borough name"""
    columns = ['place', 'ARROND_NOM', 'ESSENCE_ANG']
    df.loc[:, 'INV_TYPE'] = df.loc[:, 'INV_TYPE'].replace({"H": 0, "R": 1})
    df = pd.get_dummies(data=df, columns=columns)
    return df


def plot_corr(df):
    corr = df.corr()
    mask = np.zeros_like(corr, dtype=np.bool8)
    mask[np.triu_indices_from(mask)] = True
    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(220,10, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap= cmap, vmax=0.3, center=0,
                square=True)
    plt.title('Correlation plot')
    return


cluster_data = cluster_processing(cluster_df)
scores = [KMeans(n_clusters=i+2).fit(cluster_data).inertia_ for i in range(10)]
sns.lineplot(np.arange(2, 12), scores)
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Inertia of k-means versus number of clusters')
plot_corr(cluster_data)
plt.show()


# 9  Differences in type of trees in different areas
trees_type_dif = trees_new.groupby(by=['ARROND_NOM', 'ESSENCE_ANG'],
                                   sort=True,
                                   as_index=False)['ESSENCE_ANG'].count()

ahuntsic = trees_new.loc[trees_new['ARROND_NOM'] == 'Ahuntsic - Cartierville']
ahuntsic_tree = ahuntsic['ESSENCE_ANG'].value_counts()
ahuntsic_tree_2 = ahuntsic.groupby('ESSENCE_ANG', as_index=False).count().max()
ahuntsic_test = ahuntsic.loc[ahuntsic['ESSENCE_ANG'] == 'spruce Iseli Fastigiata']

for x in trees_new['ARROND_NOM'].unique():
    area = trees_new.loc[trees_new['ARROND_NOM']== x]
    area_trees = area['ESSENCE_ANG'].value_counts().head(2)
    # print('Area:', x, '\\', 'Most planted:', area_trees)
