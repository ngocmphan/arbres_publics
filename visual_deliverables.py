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


path = "/Users/ngocphan/PycharmProjects/arbres_publics/" \
       "limites-administratives-agglomeration-nad83.geojson"

gdf = geopandas.read_file(path)
gdf["geometry"] = gdf["geometry"].to_crs(epsg=4326)
gdf.to_file("montreal_island.json", driver="GeoJSON")


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

df_final = gdf.merge(viz_choropleth, left_on="NOM_OFFICIEL",
                     right_on="ARROND_NOM", how="outer")
df_final.reset_index(inplace=True)

m = folium.Map(location=[45.50, -73.62], zoom_start=10)
folium.Choropleth(
    geo_data="montreal_island.json",
    data=df_final,
    columns=['NOM_OFFICIEL', 'INV_TYPE'],
    key_on="feature.properties.NOM_OFFICIEL",
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Number of trees',
    nan_fill_color="White"
).add_to(m)

m.save("Choropleth on Montreal Island.html")
