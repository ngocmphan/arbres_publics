from data_prep import trees_new
import folium
import pandas as pd
import geopandas


def viz_map_option(item):
    if 'borough' == item:
        print(trees_new['ARROND_NOM'].unique())
    elif 'place' == item:
        print(trees_new['place'].unique())
    else:
        print('Boroughs', trees_new['ARROND_NOM'].unique())
    return


path = "limites-administratives-agglomeration-nad83.json"

gdf = geopandas.read_file(path)
# print(gdf["NOM_OFFICIEL"].unique())

borough_names_to_replace = list(trees_new['ARROND_NOM'].unique())

borough_names_adjusted = ['Ahuntsic-Cartierville',
                          'Villeray–Saint-Michel–Parc-Extension',
                          'Rosemont–La Petite-Patrie',
                          'Mercier–Hochelaga-Maisonneuve',
                          'Le Plateau-Mont-Royal',
                          'Ville-Marie',
                          'Côte-des-Neiges–Notre-Dame-de-Grâce',
                          'Le Sud-Ouest',
                          'Rivière-des-Prairies–Pointe-aux-Trembles',
                          'Saint-Léonard',
                          'LaSalle', 'Verdun', 'Pierrefonds-Roxboro',
                          'Saint-Laurent', 'Anjou', 'Montréal-Est']

trees_choropleth = trees_new.replace(borough_names_to_replace,
                                     borough_names_adjusted)

top_10_trees = list(trees_new['ESSENCE_ANG'].value_counts()[:10].index)

type_selected = ["Silver Maple"]
trees_choropleth = trees_choropleth[trees_choropleth["ESSENCE_ANG"]
    .isin(type_selected)]
viz_choropleth = trees_choropleth.groupby(["ARROND_NOM"], as_index=False).count()
viz_choropleth = viz_choropleth[['ARROND_NOM', "INV_TYPE"]]

list_not_in = []
for value in gdf['NOM_OFFICIEL']:
    if value in borough_names_adjusted:
        None
    else:
        list_not_in.append(value)

print(list_not_in)

df_new = pd.DataFrame({"ARROND_NOM": list_not_in, "INV_TYPE": 0})
viz_choropleth = viz_choropleth.append(df_new).reset_index()

m = folium.Map(location=[45.50, -73.62], zoom_start=5)
folium.Choropleth(
    geo_data=open(path).read(),
    data=viz_choropleth,
    columns=['ARROND_NOM', 'INV_TYPE'],
    key_on="feature.properties.NOM_OFFICIEL",
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Number of trees').add_to(m)

m.save("Choropleth of {} on Montreal Island.html".format(type_selected))
