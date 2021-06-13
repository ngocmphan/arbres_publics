from data_prep import trees_new
import matplotlib.pyplot as plt
import seaborn as sns

# Questions

# 1 Comparison between on-road and off-road trees:
no_on_off_road = trees_new['INV_TYPE'].value_counts()

# 2 Top 3 areas with most trees
areas = trees_new['ARROND_NOM'].value_counts()

# 3 Top 3 most planted trees
trees_type = trees_new['ESSENCE_ANG'].value_counts()

# 4 Type of earth where trees are most planted
earth_type = trees_new['place'].value_counts()
print(trees_new.info())

# 5 Compare the DHP of trees in different areas
box_plot = trees_new.boxplot(column=['DHP'], by=['ARROND_NOM'], fontsize=8)
ax = sns.boxplot(x='ARROND_NOM', y='DHP', data=trees_new)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.close()

histo = sns.displot(trees_new, x='DHP', hue='ARROND_NOM', kind='kde',
                    fill=True,
                    height=5, aspect=5)
plt.show()
