import pandas 


trees = pandas.read_csv("arbres-publics.csv", dtype={'ARROND_NOM': str, 'Rue': str}, low_memory=False)

print(trees.info())