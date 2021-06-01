from data_prep import trees_new

# Questions

# 1 Comparison between on-road and off-road trees:
no_on_off_road = trees_new['INV_TYPE'].value_counts()

# 2 Top 3 areas with most trees
areas = trees_new['ARROND_NOM'].value_counts()

# 3 Top 3 most planted trees
trees_type = trees_new['ESSENCE_ANG'].value_counts()

# 4 Type of earth where trees are most planted
earth_type = trees_new['place'].value_counts()
print(earth_type)
print(trees_new.info())

