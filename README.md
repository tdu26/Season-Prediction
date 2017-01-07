# Season-Prediction

An intuitive hypothesis : People’s tastes and feelings change from seasons to seasons, so people have different preferences when come to food selections in different seasons. We would like to find out if some food or drink have high correlation with sepecific season and would like to predict season given restaurant type and reviews. Thus, we are interested in:

                                           Season <= restaurant type + reviews

# Data source

Yelp Dataset Challenge. https://www.yelp.com/dataset_challenge

The Challenge Dataset details:
- 2.7M reviews and 649K tips by 687K users for 86K businesses
- 566K business attributes, e.g., hours, parking availability, ambience.
- Social network of 687K users for a total of 4.2M social edges.
- Aggregated check-ins over time for each of the 86K businesses
- 200,000 pictures from the included businesses

# Data understanding
We extracted 26805 business information of restaurants from 86K businesses, and focused on 211001 reviews on these restaurants.
Among 211001 entries, 70% is used for training and 30% is used for testing. 
