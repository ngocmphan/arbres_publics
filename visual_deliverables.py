from data_prep import trees_new
import folium
import pandas as pd

# Excluding NaN rows
trees_new = trees_new.dropna(subset=['Longitude', 'Latitude'], axis=0)


# Create Map
m = folium.Map(location=[45.513, -73.612], zoom_start=11,
               titles='Montreal maps of trees')

for index, row in trees_new.iterrows():
    location = [row['Latitude'], row['Longitude']]
    folium.Marker(location).add_to(m)

m.save(outfile='maps_of_trees.html')
