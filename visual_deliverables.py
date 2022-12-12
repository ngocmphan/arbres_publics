from data_prep import trees_new
import folium
import pandas as pd
import geopandas


path = "/Users/ngocphan/PycharmProjects/arbres_publics/" \
       "limites-administratives-agglomeration-nad83.geojson"


def geo_data():
    gdf = geopandas.read_file(path)
    gdf["geometry"] = gdf["geometry"].to_crs(epsg=4326)
    gdf.to_file("montreal_island.json", driver="GeoJSON")
    geo_path = "montreal_island.json"
    return gdf, geo_path


def trees_data_prep():
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
    return trees_choropleth


top_10_trees = list(trees_new['ESSENCE_ANG'].value_counts()[:10].index)
print(top_10_trees)


def question_2b():
    trees_type = trees_new['ESSENCE_ANG'].value_counts()
    trees_type_df = pd.DataFrame(trees_type).reset_index()
    trees_type_df = trees_type_df.rename(columns={"ESSENCE_ANG": "count",
                                         'index': "ESSENCE_ANG"})
    maple_tree = trees_type_df[
        trees_type_df['ESSENCE_ANG'].str.contains('Maple')]
    list_maple_tree = maple_tree['ESSENCE_ANG'].unique()
    return list_maple_tree


maple_list = list(question_2b())


def choropleth_plotting(value, title):
    """Function to create choropleth map with selected tree type.
    The input is a list including one or more tree types"""

    # visualization data preparation with boroughs filter:
    type_selected = value
    trees_choropleth = trees_data_prep()
    trees_choropleth = trees_choropleth[trees_choropleth["ESSENCE_ANG"]
        .isin(type_selected)]
    viz_choropleth = trees_choropleth.groupby(["ARROND_NOM"],
                                              as_index=False).count()
    viz_choropleth = viz_choropleth[['ARROND_NOM', "INV_TYPE"]]

    # final visualization data:
    gdf, geo_path = geo_data()

    df_final = gdf.merge(viz_choropleth, left_on="NOM_OFFICIEL",
                         right_on="ARROND_NOM", how="outer")
    df_final.reset_index(inplace=True)
    bins = list(df_final["INV_TYPE"].quantile([0, 0.25, 0.5, 0.75, 1]))
    if len(value) < 2:
        # Choropleth mapping:
        print(title)
        m = folium.Map(location=[45.50, -73.62], zoom_start=10)
        folium.Choropleth(
            geo_data="montreal_island.json",
            name=value,
            data=df_final,
            columns=['NOM_OFFICIEL', 'INV_TYPE'],
            key_on="feature.properties.NOM_OFFICIEL",
            fill_color='YlGn',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Number of trees',
            nan_fill_color="White",
            bins=bins
        ).add_to(m)

        m.save("Choropleth of trees {} on Montreal Island.html".format(value))
    else:
        print(title)
        m = folium.Map(location=[45.50, -73.62], zoom_start=10)
        folium.Choropleth(
            geo_data="montreal_island.json",
            name=title,
            data=df_final,
            columns=['NOM_OFFICIEL', 'INV_TYPE'],
            key_on="feature.properties.NOM_OFFICIEL",
            fill_color='YlGn',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Number of trees',
            nan_fill_color="White",
            bins=bins
        ).add_to(m)
        m.save("Choropleth of {} trees Montreal Island.html".format(title))


choropleth_plotting(["Silver Maple"], "1 - Silver Maple")
choropleth_plotting(["Norway Maple"], "2 - Norway Maple")
choropleth_plotting(['Red Ash'], "3 - Red Ash")
choropleth_plotting(maple_list, "All maple trees")

