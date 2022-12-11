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


viz_map_option("a")

path = "limites-administratives-agglomeration-nad83.geojson"

gdf = geopandas.read_file(path)
print(gdf.columns)
print(gdf["NOM_OFFICIEL"].unique())

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



