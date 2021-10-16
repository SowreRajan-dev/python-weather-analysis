import pandas as pd

# importing the weather dataset

data = pd.read_csv(
    r'C:\\programming\\python\weatherAnalysis\\python-weather-analysis\\WeatherData.csv')

# Exploring data...

# head() - shows N no. of rows in data
print("No of rows in data set:\n ", data.head())

# shape - shows total number of rows and columns
print("No of rows and columns in data set:\n ", data.shape)


# index - shows index of data set
print("Index of data set:\n", data.index)

# columns
print("Columns of data set:\n", data.columns)

# dtypes - shows data types of Columns
print("dataType  of  columns in data set:\n", data.dtypes)

# unique() - shows unique values in a Columns
print("unique values in weather columns:\n", data['Weather'].unique())

# nunique - shows number of unique values in each columns
print("unique values in data set:\n", data.nunique())

# count - total number of non null in each Columns
print("count of non null values in data set:\n", data.count)


# count - counts unique values and return itts count
print("count of unique_values in data set:\n", data['Weather'].value_counts)

# info() - provoides basic info about data set
print("Info of data set:\n", data.info())
