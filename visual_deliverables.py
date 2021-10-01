from data_prep import trees_new
import folium
import pandas as pd


def viz_map_option(item):
    if 'borough' == item:
        print(trees_new['ARROND_NOM'].unique())
    elif 'place' == item:
        print(trees_new['place'].unique())
    else:
        print('Boroughs', trees_new['ARROND_NOM'].unique())
        print('Placement', trees_new['place'].unique())
    return


def viz_map(inv, place, borough='Rosemont - La Petite-Patrie'):
    """Creating interactive folium map by borough name, type, and placement:

    Parameters
    ----------
    borough : Name of the boroughs - 16 boroughs
    inv     : "R" - on road, "H" - off road
    place   : Placement of the trees - 8 placements

    Returns
    ---------
    Interactive visualization map
    """
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

    m.save(outfile='Trees in {name} on {road} on {placement}.html'
           .format(name=borough, road=inv, placement=place))
    return


viz_map_option('a')

viz_map('R', 'parterre')
viz_map('R', 'banquette')
viz_map('R', 'terre-plein')
viz_map('R', 'trottoir')
viz_map('R', 'parc')
viz_map('R', 'saillie')
viz_map('R', 'îlot de verdure')

viz_map('H', 'parterre')
viz_map('H', 'banquette')
viz_map('H', 'terre-plein')
viz_map('H', 'trottoir')
viz_map('H', 'parc')
viz_map('H', 'saillie')
viz_map('H', 'îlot de verdure')