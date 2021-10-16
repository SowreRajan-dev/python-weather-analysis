import pandas as pd

# importing the weather dataset

data = pd.read_csv(
    r'C:\\programming\\python\weatherAnalysis\\python-weather-analysis\\WeatherData.csv')


# Data Analysis from the data set
print("1. Find  all the unique 'Wind Speed' values in the data.\n")
print("The no. of unique Wind Speed values are : \n",
      data['Wind Speed_km/h'].nunique())
print("\nand the values are ...\n", data['Wind Speed_km/h'].unique())

print("\n")

print("2. Find the number of times when the 'Weather is exactly Clear'.\n")
# filtering the data
data.head(2)
print("the number of times the Weather is exactly clear is:\n",
      data[data.Weather == 'Clear'])
print("\n")


print("3. Find the number of times when the 'Wind speed is exactly 4 km/h'.\n")
data.head(2)
print("The number of times when the Wind speed is exactly 4km/h are:\n",
      data[data['Wind Speed_km/h'] == 4])
print("\n")

print("4. Find out all the Null Values in the data set.\n")
data.head(2)
print("The Null Values in data set ...\n", data.isnull().sum())
print("\n")


print("5. Rename the column name 'Weather' to 'Weather Condition'.\n")
data.head(2)
data.rename(columns={'Weather': 'Weather Condition'}, inplace=True)
print(data.head(3))

print("6. What is mean 'Visiblity'.\n")
data.head(2)
print("the mean is : ", data['Visibility_km'].mean())
print("\n")

print("6. What is standard deviation of 'Pressure' in this data.\n")
data.head(2)
print("the standard deviation is : ", data['Press_kPa'].std())
print("\n")
