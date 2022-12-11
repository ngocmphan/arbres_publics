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

