import pandas 


trees = pandas.read_csv("arbres-publics.csv", dtype={'ARROND_NOM': str, 'Rue': str}, low_memory=False)

#print(trees.info())
print(trees['ARROND_NOM'].value_counts())
print(trees['ESSENCE_ANG'].value_counts())
print(trees['ESSENCE_ANG'].nunique())
