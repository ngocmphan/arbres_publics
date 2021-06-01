from data_prep import trees_new
import folium
import pandas as pd

# Excluding NaN rows
trees_new = trees_new.dropna(subset=['Longitude', 'Latitude'], axis=0)


# Create Map
m = folium.Map(location=[45.513, -73.612], zoom_start=10,
               titles='Montreal maps of trees')

tooltip = "I'm a tree"

for index, row in trees_new.iterrows():
    location = [row['Latitude'], row['Longitude']]
    marker = folium.Marker(location, tooltip=tooltip)
    m.add_child(marker)

m.save(outfile='maps_of_trees.html')
