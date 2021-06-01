from data_prep import trees_new
import folium
import pandas as pd

# Excluding NaN rows
trees_new = trees_new.dropna(axis=0)

# Create Map
m = folium.Map(location=[45.513, -73.612], zoom_start=8,
               titles='Montreal maps of trees')

tooltip = "I'm a tree"

for index, row in trees_new.iterrows():
    location = [row['Longitude'], row['Latitude']]
    folium.Marker(location, tooltip=tooltip).add_to(m)

m.save(outfile='maps_of_trees.html')


