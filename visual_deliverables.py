from data_prep import trees_new
import folium
import pandas as pd
print(trees_new['ARROND_NOM'].unique())

# Selecting vars
trees_borough = trees_new[trees_new['ARROND_NOM'] ==
                          'Rosemont - La Petite-Patrie']
trees_road = trees_borough[trees_borough['INV_TYPE'] == 'R']
trees_placement = trees_road[trees_road['place'] == 'parc']

# Drop NaN
trees_viz = trees_placement.dropna(subset=['Longitude', 'Latitude'], axis=0)
trees_viz = trees_viz[['Longitude', 'Latitude']]

# Create Map
m = folium.Map(location=[45.588457730918, -73.56167346642063], zoom_start=15,
               titles='Montreal maps of trees')

for index, row in trees_viz.iterrows():
    location = [row['Latitude'], row['Longitude']]
    folium.Marker(location, tooltip=location).add_to(m)


m.save(outfile='maps_of_trees.html')


def viz_map(borough, inv, place):
    # Selecting vars
    trees_borough = trees_new[trees_new['ARROND_NOM'] ==
                              borough]
    trees_road = trees_borough[trees_borough['INV_TYPE'] == inv]
    trees_placement = trees_road[trees_road['place'] == place]

    # Drop NaN
    trees_viz = trees_placement.dropna(subset=['Longitude', 'Latitude'], axis=0)
    trees_viz = trees_viz[['Longitude', 'Latitude']]

    # Creating maps
    m = folium.Map(location=[45.588457730918, -73.56167346642063],
                   zoom_start=15,
                   titles='Montreal maps of trees')

    for index, row in trees_viz.iterrows():
        location = [row['Latitude'], row['Longitude']]
        folium.Marker(location, tooltip=location).add_to(m)

    m.save(outfile=''.format(borough, inv, place))
    return
