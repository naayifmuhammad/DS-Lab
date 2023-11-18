import pandas as pd
#read a csv file
ufo = pd.read_csv('http://bit.ly/uforeports')
print("Overview of UFO data reports: ")
print(ufo.head())
print()
15
#series
print("Cityseries(sorted):")
print(ufo.City.sort_values())
print()
ufo['Location'] = ufo.City + ', ' + ufo.State
print("After creating a new 'Location' Series : ")
print(ufo.head())
print()
print("Calculate summary statistics : ")
print(ufo.describe())
print()
print("Column names of ufo dataframe : ",ufo.columns)
print()
# rename two of the columns by using the 'rename' method
ufo.rename(columns={'Colors Reported':'Colors_Reported',
'ShapeReported':'Shape_Reported'},inplace=True)
print("Column name of ufo dataframe after renaming two column names :
",ufo.columns)
print()
# remove multiple columns at once
ufo.drop(['City', 'State'], axis=1, inplace=True)
print("Column name of ufo dataframe after removing two columns(city,state) :
",ufo.columns)
print()
# remove multiple rows at once (axis=0 refers to rows)
ufo.drop([0, 1], axis=0, inplace=True)
print("ufo dataframe after deleting first two rows: ")
print(ufo.head())