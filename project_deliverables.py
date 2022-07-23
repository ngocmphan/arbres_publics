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
import statistics as stat
import mca
from pylab import *

# Questions

# 1 Comparison between on-road and off-road trees:


def question_1():
    no_on_off_road = trees_new['INV_TYPE'].value_counts()
    print(no_on_off_road)


# 2 Top 3 most planted trees


def question_2():
    trees_type = trees_new['ESSENCE_ANG'].value_counts()
    top_10_trees = list(trees_type[:15].index)
    least_10_trees = list(trees_type[::-1][:10].index)
    trees_type_df = pd.DataFrame(trees_type).reset_index()
    trees_type_df = trees_type_df.rename(columns={'ESSENCE_ANG': 'count',
                                                  'index': 'ESSENCE_ANG'})
    # Create dataframe with top 15 trees, and remaining in "others":
    top_trees = {}
    values = 0
    for index, row in trees_type_df.iterrows():
        if row['ESSENCE_ANG'] in top_10_trees:
            top_trees.update({row['ESSENCE_ANG']: row['count']})
        else:
            values += row['count']
            top_trees.update({'other': values})
    top_trees_df = pd.DataFrame(top_trees.items(),
                                columns=['ESSENCE_ANG', 'count'])
    # print(top_trees)
    # print(top_trees_df)
    print(least_10_trees)


# 2a Variety of trees

def question_2a():
    tree_variety = trees_new['ESSENCE_ANG'].unique()
    print(len(tree_variety))

# 2b Percentage of maple trees population


def question_2b():
    trees_type = trees_new['ESSENCE_ANG'].value_counts()
    trees_type_df = pd.DataFrame(trees_type).reset_index()
    trees_type_df = trees_type_df.rename(columns={"ESSENCE_ANG": "count",
                                         'index': "ESSENCE_ANG"})
    maple_tree = trees_type_df[trees_type_df['ESSENCE_ANG'].str.contains('Maple')]
    print(sum(maple_tree['count']))
    print(len(maple_tree['ESSENCE_ANG'].unique()))


# 3 Type of earth where trees are most planted

def question_3():
    earth_type = trees_new['place'].value_counts()
    print(earth_type)


# 4 95% Confidence interval for DHP of trees.


def question_4(option):
    """ Question 5:
    If option is inputted: Display distribution plot of trees diameter.
    If option is not indicated: 95% Confidence interval of trees diameter.
    """
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


# 4a Box plot of tree population
def question_4a():
    box = plt.boxplot(x=trees_new['DHP'], showmeans=True, meanline=True)
    plt.title('Boxplot of tree population in Greater Montreal Area')
    median = [line.get_data() for line in box['medians']][0]
    text(median[0][1]+0.05, median[1][0]-4, '%.1f' % median[1][0],
         horizontalalignment='right', verticalalignment='center')
    mean = [line.get_data() for line in box['means']][0]
    text(mean[0][1]+0.05, mean[1][0]+3, '%.1f' % mean[1][0],
         horizontalalignment='right', verticalalignment='center')
    upper_cap = [line.get_data() for line in box['caps']][0]
    lower_cap = [line.get_data() for line in box['caps']][1]
    text(upper_cap[0][1]+0.05, upper_cap[1][0], '%.1f' % upper_cap[1][0],
         horizontalalignment='right', verticalalignment='center')
    text(lower_cap[0][1]+0.05, lower_cap[1][0], '%.1f' % lower_cap[1][0],
         horizontalalignment='right', verticalalignment='center')
    plt.show()


# 4b Box plot of trees types for top 12 trees
def question_4b():
    # With outliers
    trees_type = trees_new['ESSENCE_ANG'].value_counts()
    top_12_trees = list(trees_type[:12].index)
    top_12_df = trees_new[trees_new['ESSENCE_ANG'].isin(top_12_trees)]
    plt.figure()
    box = sns.boxplot(x='ESSENCE_ANG', y='DHP', data=top_12_df, showmeans=True,
                      meanprops={'markeredgecolor': 'black'})
    plt.title("Boxplots of top 12 tree types in GMA with outliers")
    sns.set(font_scale=0.5)
    plt.xticks(rotation=20, fontsize=12)
    plt.show()

    # Without outliers
    plt.figure()
    plt.title("Boxplots of top 12 tree types in GMA without outliers",
              fontsize=12)
    box_without = sns.boxplot(x='ESSENCE_ANG', y='DHP', data=top_12_df,
                      showfliers=False, showmeans=True,
                              meanprops={'markeredgecolor': 'black'})
    sns.set(font_scale=0.5)
    plt.xticks(rotation=20, fontsize=12)
    plt.yticks(fontsize=12)
    plt.ylabel("DHP", fontsize=12)
    plt.show()


# 5 DHP measure of the trees on road and off road


def question_5(option):
    """Question 6:
    If Option is inputted: Display distribution plot of on and off road trees,
     and box plot of on and off road trees.
    Option not indicated: 95% Confidence interval of on and off road trees.
     """
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

        box_plot_on_off = sns.boxplot(x='INV_TYPE', y='DHP', data=trees_new)
        plt.title('Box plot of on and off road trees')
        plt.show()
    else:
        CI_mtl_road = 'Confidence interval of on road trees: [{0:2f}, {1:2f}]'.\
            format(mean_on_road - 1.96*multiplier_on_road,
                   mean_on_road + 1.96*multiplier_on_road)

        CI_mtl_off_road = 'Confidence interval of ' \
                          'off road trees: [{0:2f}, {1:2f}]'\
            .format(mean_off_road - 1.96*multiplier_off_road,
                    mean_off_road + 1.96*multiplier_off_road)
        print(CI_mtl_off_road, CI_mtl_road)

# 6 Profile the placement of the trees


def question_6():
    box_plot_place = sns.boxplot(x='place', y='DHP', data=trees_new)
    plt.title('Box plot of different trees placements')
    plt.show()

# 7 Clustering to identify group of trees


def question_7():
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
        eva_kmeans = silhouette_score(cluster_data, kmeans.labels_,
                                      metric='euclidean',
                                      sample_size=1000)
        print(eva_kmeans)
        eva_normalized = silhouette_score(normalized_vector,
                                          normalized_kmeans.labels_,
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
    selected_columns = list(results.sort_values('std', ascending=False)
                            .head(7).Variable.values) + ['kmeans_norm']

    # plot data

    def cluster_result():
        tidy = df_scaled[selected_columns].melt(id_vars='kmeans_norm')
        fig, ax = plt.subplots(figsize=(15, 5))
        sns.barplot(x='kmeans_norm', y='value', hue='variable', data=tidy,
                    palette='Set3')
        plt.legend(loc='upper right')
        plt.show()

    cluster_result()


# 8 Top 3 areas with most trees


def question_8():
    areas = trees_new['ARROND_NOM'].value_counts()
    print(areas)


# 9  Differences in type of trees in different areas

def question_9():
    trees_by_area = {}
    for x in trees_new['ARROND_NOM'].unique():
        area = trees_new.loc[trees_new['ARROND_NOM'] == x]
        area_trees = area['ESSENCE_ANG'].value_counts().head(3).index
        area_dict = {x: list(area_trees)}
        trees_by_area.update(area_dict)
    trees_name_area = pd.DataFrame.from_dict(trees_by_area, orient='index',
                                             columns=['First', 'Second',
                                                      'Third'])
    print(trees_name_area['First'], trees_name_area['Second'],
          trees_name_area['Third'])


# 10 Compare the DHP of trees in different areas


def question_10(option):
    """ Question 10:
    Option "box": Display box plot of DHP by boroughs.
    Option "histo": Display histogram plot of DHP by boroughs """
    if option == 'box':
        ax = sns.boxplot(x='ARROND_NOM', y='DHP', data=trees_new, showmeans=True,
                         showfliers=False, meanprops={'markeredgecolor': 'black'})
        ax.set_xticklabels(ax.get_xticklabels(), rotation=20, ha="right")
        plt.title("Boxplot of DHP by GMA neighborhoods")
        plt.xticks(fontsize=7)
        plt.show()
    elif option == 'histo':
        histo = sns.displot(trees_new, x='DHP', hue='ARROND_NOM', kind='kde',
                            fill=True,
                            height=5, aspect=5)
        plt.show()


# 14 Sufficiency of green scenery on meeting population needs
def question_14():
    population = 2025928
    population_needs = population*7.5
    trees = trees_new['EMP_NO'].count()
    sufficiency = trees*100/population_needs
    trees_per_person = trees/population
    person_per_tree = population/trees
    print(population_needs)
    print(sufficiency)
    print("Trees per person", trees_per_person)
    print("Person per tree", person_per_tree)


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

    # trees per person by neighborhood
    trees_by_area['tree_per_person'] = trees_by_area['ESSENCE_ANG'] / \
                                       trees_by_area['pop_2021']
    print(trees_by_area['ESSENCE_ANG'])
    print(trees_by_area[['ARROND_NOM', 'tree_per_person']])


question_10("box")
