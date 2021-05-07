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
| Rue| Characterical | 218207| Name of the road for trees on the road.| X|
| Cote| Categorical  | 218207| Side of the road (N- North, S - South, E - East, O - West)| X|
| No_civique| | 171194| Numeral of the resident where the off road trees located| X|
|Emplacement| Character  | 317844| Type of earth/dirt that the trees located on| X|
| Coord_X| Numerical  | 317844| x- coordinate| X|
| Coord_Y| Numerical  | 317840| y- coordinate| X|
|SIGLE| Character  | 317844| The shortened latin name of the plant.| X|
|Essence latin| Character  | 317844| Full Latin name of the plant.| X|
|Essence FR| Character  | 317844| French name of the plant.| X|
|Essence ang| Character  | 317844| English name of the plant.| X|
|DHP|Numerical | 317172| Diameter measurement of the trunc of the trees.| X|
|Date_releve| Date| 317172| Date of the latest measurement of DHP.| X|
|Date_plantation| Date| 150019| Plantation date of the trees. | X|
|Localisation| | 217913| Location of the trees from the last corner of the last establishment.| X|
|Code_parc| Numerical| 99637| Index number of the park.| X|
|Nom_parc| Character| 99637|Name of the park. | X|
|Longitude|Numerical| 317840| Longitude geolocation of each tree. | X|
|Latitude|Numerical| 317840| Latitude geolocation of each tree.| X|

The dataset can be obtained from the following source:
Abres publics sur le territoire de la Ville. Ville de Montréal. Data updated on May 03, 2021. Retrieved from: https://donnees.montreal.ca/ville-de-montreal/arbres

## Questions
* What is the percentage changes in the number of public trees?
* What is the percentage changes in public trees off the roads? (Ex: trees in parks)
* What is the percentage changes in public trees on side of the roads? 
* Which areas/districts have the most significant changes? 
* Types of trees most planted: on road vs off road
* Is there any difference in the types of trees planted in different areas?
* Which area/side of the road the trees have the biggest measure?
* Confidence interval for DHP of trees for each trees type and trees in each area/district. 


