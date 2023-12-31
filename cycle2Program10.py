import pandas as pd
# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
print("Dataframe of top-rated IMDb movies: ")
print(movies.head())
print()
print("Different ways to filter rows of a pandas DataFrame by column value: ")
print("Example : Filter rows to only show movies with a duration of atleast 200 minutes")
print("1.using for loop")
# create a list in which each element refers to a DataFrame row: True if the row satisfies
the condition,False otherwise
17
booleans = []
for length in movies.duration:
if length >= 200:
booleans.append(True)
else:
booleans.append(False)
is_long = pd.Series(booleans)
print(is_long.head())
print()
print("2.broadcasting")
print(movies[movies.duration >= 200])
print()
print("3.using 'loc' method")
print(movies.loc[movies.duration >= 200])
