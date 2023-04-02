# arbres_publics

## Topic
The topic of the project is exploring the greenery of the Greater Montreal Area with public trees to inform the public about the changes in trees and green scenery. 

## Project goal
Based on the fact that each individual needs on average seven or eight trees for air and 3-5% of trees die each year, we are assessing the number of public trees in Montreal against the number of residents currently living on Montreal Island. The project aims to determine if the number of trees are appropriate for the current population living in Montreal. In addition, exploration regarding the wellness and diversity of the trees planted is conducted. 

## Data sources and variables
The data set obtained from Ville de Montreal with information regarding public trees. The data set included 22 variables with maximum of 317,844 observations with a time period from 1989 to current year. The dataset was made available to the public on July 2012.

The data set has missing observations for 12 variables. In addition, the data source disclosed that some geolocation and other information in the system might not be precise or up-to-date for some trees.

| Variable| Variable type| Number of obs| Information| Used|
| --------|--------------|--------------|------------|-----|
| INV Type| Categorical  | 317844| Type of trees: H- off road, R-on road| X|
| EMP No | Numerical  | 317844| Unique trees number in government database| X|
| ARROND| Numerical  | 317844| Numeral of each district/area| X|
| ARROND_NOM| Characterical | 317844| District/area name| X|
| Rue| Characterical | 218207| Name of the road for trees on the road.| |
| Cote| Categorical  | 218207| Side of the road (N- North, S - South, E - East, O - West)| |
| No_civique| | 171194| Numeral of the resident where the off road trees located| |
|Emplacement| Character  | 317844| Type of earth/dirt that the trees located on| X|
| Coord_X| Numerical  | 317844| x- coordinate| |
| Coord_Y| Numerical  | 317840| y- coordinate| |
|SIGLE| Character  | 317844| The shortened latin name of the plant.| |
|Essence latin| Character  | 317844| Full Latin name of the plant.| |
|Essence FR| Character  | 317844| French name of the plant.| |
|Essence ang| Character  | 317844| English name of the plant.| X|
|DHP|Numerical | 317172| Diameter measurement of the trunc of the trees.| X|
|Date_releve| Date| 317172| Date of the latest measurement of DHP.| |
|Date_plantation| Date| 150019| Plantation date of the trees. | |
|Localisation| | 217913| Location of the trees from the last corner of the last establishment.| |
|Code_parc| Numerical| 99637| Index number of the park.| |
|Nom_parc| Character| 99637|Name of the park. | |
|Longitude|Numerical| 317840| Longitude geolocation of each tree. | X|
|Latitude|Numerical| 317840| Latitude geolocation of each tree.| X|

The dataset can be obtained from the following source:
Abres publics sur le territoire de la Ville. Ville de Montréal. Data updated on May 03, 2021. Retrieved from: https://donnees.montreal.ca/ville-de-montreal/arbres

## Tools used
* Python libraries: Pandas, Geopandas, Folium, Matplotlib, sklearn, seaborn

## Deliverables

### Visualization
* Choropleth map of all the trees on Montreal Island, the top three most prevalent types of trees and maple syrup trees.

### Quantitative deliverables
#### Trees profile
* Types of trees most planted: on road versus off road
* In general, what are the most planted trees?
* In general, what are the types of land that trees were most planted on?
* Confidence interval for DHP of trees.  
* Generally, how big are the trees on road versus off road?
* Profile the placements of trees. 
* Conduct unsupervised learning - clustering to identify groups of trees. 
#### Area differences
* What are the top 3 areas with most trees?
* Is there any difference in the types of trees planted in different areas?
* On average, how big are the trees in different areas? Compare.
* Confidence interval for DHP of trees for each tree type
* Is there a significant difference in the number of trees in different areas?
* Does the type of earth where the trees were planted depend on the area? 
#### Sufficiency of trees populated
* Are the number of trees sufficient in general for Montreal area as a whole?
* Compare sufficiency by area. 

### Conclusion
Visit the following project Github pages for results: https://ngocmphan.github.io/arbres_publics/

