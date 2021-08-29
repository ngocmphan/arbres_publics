# Data handling
from data_prep import trees_new
from math import sqrt
import numpy as np
import pandas as pd
# visualization
import matplotlib.pyplot as plt
import seaborn as sns
# Clustering
from sklearn.cluster import KMeans, DBSCAN
from sklearn import preprocessing
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler
import mca

# Questions

# 1 Comparison between on-road and off-road trees:


def question_1():
    no_on_off_road = trees_new['INV_TYPE'].value_counts()
    print(no_on_off_road)

# 2 Top 3 areas with most trees


def question_2():
    areas = trees_new['ARROND_NOM'].value_counts()

# 3 Top 3 most planted trees


def question_3():
    trees_type = trees_new['ESSENCE_ANG'].value_counts()
    top_10_trees = list(trees_type[:10].index)
    print("Trees count:", trees_type)
    print('Top 10 trees:', top_10_trees)

# 4 Type of earth where trees are most planted


def question_4():
    earth_type = trees_new['place'].value_counts()
    print(earth_type)

# 6 Compare the DHP of trees in different areas


def question_10(option):
    """Display box plot or histogram"""
    if option == 'box':
        box_plot = trees_new.boxplot(column=['DHP'], by=['ARROND_NOM'], fontsize=8)
        ax = sns.boxplot(x='ARROND_NOM', y='DHP', data=trees_new)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
        plt.show()
    elif option == 'histo':
        histo = sns.displot(trees_new, x='DHP', hue='ARROND_NOM', kind='kde',
                            fill=True,
                            height=5, aspect=5)
        plt.show()

# 5 95% Confidence interval for DHP of trees.


def question_5(option):
    std = trees_new['DHP'].std()
    mean = trees_new['DHP'].mean()
    n = trees_new['DHP'].count()
    multiplier = std / sqrt(n)
    if option is True:
        fig, ax = plt.subplots()
        sns.histplot(trees_new, x='DHP').set_title('Distribution plot of trees diameter')
        ax.set_xlim(0, 120)
        plt.show()
    else:
        ci_mtl = 'Confidence interval of Montreal trees: [{0:2f}, {1:2f}]'\
            .format(mean-1.96*multiplier, mean+1.96*multiplier)
        print('95% confidence interval for DHP of trees: {}'.format(ci_mtl) )

# 6 DHP measure of the trees on road and off road


def question_6(option):
    on_road = trees_new.loc[trees_new['INV_TYPE'] == 'R']
    off_road = trees_new.loc[trees_new['INV_TYPE'] == 'H']

    on_road_place = on_road['Emplacement'].value_counts()
    off_road_place = off_road['Emplacement'].value_counts()

    std_on_road = on_road['DHP'].std()
    std_off_road = off_road['DHP'].std()

    mean_on_road = on_road['DHP'].mean()
    mean_off_road = off_road['DHP'].mean()

    n_on_road = on_road['DHP'].count()
    n_off_road = off_road['DHP'].count()

    multiplier_on_road = std_on_road / sqrt(n_on_road)
    multiplier_off_road = std_off_road / sqrt(n_off_road)

    if option is True:
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
    else:
        CI_mtl_road = 'Confidence interval of on road trees: [{0:2f}, {1:2f}]'.\
            format(mean_on_road - 1.96*multiplier_on_road,
                   mean_on_road + 1.96*multiplier_on_road)

        CI_mtl_off_road = 'Confidence interval of ' \
                          'off road trees: [{0:2f}, {1:2f}]'\
            .format(mean_off_road - 1.96*multiplier_off_road,
                    mean_off_road + 1.96*multiplier_off_road)
        print(CI_mtl_off_road, CI_mtl_road)

# 7 Profile the placement of the trees


def question_7():
    box_plot_place = sns.boxplot(x='place', y='DHP', data=trees_new)
    plt.title('Box plot of different trees placements')
    plt.show()

# 8 Clustering to identify group of trees

top_10_trees = list(trees_new['ESSENCE_ANG'].value_counts()[:10].index)
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
# Non-normalized k-means


def non_norm_kmeans():
    scores = [KMeans(n_clusters=i + 2).fit(cluster_data).inertia_ for i in
              range(10)]
    sns.lineplot(x=np.arange(2, 12), y=scores)
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.title('Inertia vs Number of clusters kmeans')
    plt.show()


kmeans = KMeans(n_clusters=4).fit(cluster_data)

# Normalized k-means


def norm_kmeans():
    normalized_vector = preprocessing.normalize(cluster_data)
    normalized_scores = [KMeans(n_clusters=i+2).fit(normalized_vector).inertia_ for i in range(10)]
    sns.lineplot(x=np.arange(2, 12), y=normalized_scores)
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.title('Inertia vs Number of clusters kmeans')
    plt.show()  # 4 or 5 clusters


normalized_vector = preprocessing.normalize(cluster_data)
normalized_kmeans = KMeans(n_clusters=4).fit(normalized_vector)

# clustering: DBSCAN


def dbscan():
    min_samples = cluster_data.shape[1]+1
    dbscan = DBSCAN(eps=6, min_samples=min_samples).fit(cluster_data)
    print(dbscan.labels_.unique())
# Evaluations


def evaluation():
    eva_kmeans = silhouette_score(cluster_data, kmeans.labels_, metric='euclidean',
                                  sample_size=1000)
    print(eva_kmeans)
    eva_normalized = silhouette_score(normalized_vector, normalized_kmeans.labels_,
                                      metric='cosine', sample_size=1000)
    print(eva_normalized)


# Unique features
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(cluster_data))
df_scaled.columns = cluster_data.columns
df_scaled['kmeans_norm'] = normalized_kmeans.labels_

df_mean = df_scaled.loc[df_scaled['kmeans_norm'] != -1, :]\
    .groupby('kmeans_norm').mean().reset_index()
results = pd.DataFrame(columns=['Variable', 'std'])
for column in df_mean.columns[1:]:
    results.loc[len(results), :] = [column, np.std(df_mean[column])]
selected_columns = list(results.sort_values('std', ascending=False).head(7).Variable.values) + ['kmeans_norm']

# plot data


def cluster_result():
    tidy = df_scaled[selected_columns].melt(id_vars='kmeans_norm')
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.barplot(x='kmeans_norm', y='value', hue='variable', data=tidy, palette='Set3')
    plt.legend(loc='upper right')
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
    area = trees_new.loc[trees_new['ARROND_NOM'] == x]
    area_trees = area['ESSENCE_ANG'].value_counts().head(2)
    # print('Area:', x, '\\', 'Most planted:', area_trees)


# 14 Sufficiency of green scenery on meeting population needs
def question_14(option):
    population = 4247000
    population_needs = population*7.5
    trees = trees_new['EMP_NO'].count()
    sufficiency = trees*100/population_needs
    print(population_needs)
    print(sufficiency)


# 15 Sufficiency by areas
def question_15():
    """
        Warning: Missing/incorrect data for Ile Bizard-sainte Genevieve,
        Montreal Nord, Outremont.
        """
    trees_by_area = trees_new.groupby('ARROND_NOM')[
        'ESSENCE_ANG'].count().reset_index()
    # population of the area
    trees_by_area['pop_2016'] = [134245, 42796, 166520, 76853, 104000, 78151,
                                 136024, 3850, 69297, 106734 - 3850, 139590,
                                 98828, 78305, 69229, 89170, 143853]
    trees_by_area['pop_2021'] = trees_by_area['pop_2016'] * 1.035
    # population needs
    trees_by_area['population_needs'] = trees_by_area['pop_2021'] * 7.5

    # sufficiency
    trees_by_area['sufficiency_rate'] = trees_by_area['ESSENCE_ANG'] * 100 / \
                                        trees_by_area['population_needs']

    print(trees_by_area)
