import pandas as pd
#read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print("Dataframe : ")
print(drinks.head())
print()
print("Mean beer servings across the entire dataset: ",drinks.beer_servings.mean())
print("Mean beer servings just for countries in Africa:
",drinks[drinks.continent=='Africa'].beer_servings.mean())
print()
print("Aggregate functions used with groupby: ")
print()
print("Mean beer servings for each continent:
",drinks.groupby('continent').beer_servings.mean())
print("Maximum beer servings for each continent:
",drinks.groupby('continent').beer_servings.max())
print("Multiple aggregation functions can be applied simultaneously: ")
print(drinks.groupby('continent').beer_servings.agg(['count', 'mean', 'min', 'max']))
# specifying a column to which the aggregation function should be applied is not
required
drinks.groupby('continent').mean()
# allow plots to appear in the notebook
%matplotlib inline
20
# side-by-side bar plot of the DataFrame directly above
drinks.groupby('continent').mean().plot(kind='bar')
