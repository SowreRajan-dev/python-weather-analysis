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

print("7. What is standard deviation of 'Pressure' in this data.\n")
data.head(2)
print("the standard deviation is : ", data['Press_kPa'].std())
print("\n")

print("8. What is the Variance of 'Relative Humidity' in this data.\n")
data.head(2)
print("The Variance is: ", data['Rel Hum_%'].var())
print("\n")

print("9. Find all instances when 'Snow' was recorder.\n")
data.head(2)
data['Weather Condition'].value_counts()
data[data['Weather Condition'] == 'Snow']
print("The instances are : ",
      data[data['Weather Condition'].str.contains('Snow')].tail(50))
print("\n")

print("10.Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'\n")
data.head(2)
print("The instances are :",
      data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)])
print("\n")

print("11.What is the Mean value of each column against each 'Weather Condition'\n")
data.head(2)
print("Mean value is :", data.groupby('Weather Condition').mean())
print("\n")

print("12.What is the Minimum & Maximum value of each column against each 'Weather Condition'\n")
data.head(2)
print("The Minimum value is:", data.groupby('Weather Condition').min(),
      "The Maximum value is:", data.groupby('Weather Condition').max())
print("\n")

print("13.Show all the Records where Weather Condition is Fog.\n")
data.head(2)
print("Records:", data[data['Weather Condition'] == 'Fog'])
print("\n")

print("14.Find all instances when 'Weather is clear' or 'Visibility is above 40.'\n")
data.head(2)
print("Instances are: ", data[(data['Weather Condition'] == 'Clear') | (
    data['Visibility_km'] > 40)].tail(50))
print("\n")

print("15.Find all instances when: A.'Weather is Clear' and 'Relative Humidity is greater than 50' or B.'Visibility is above 40'\n")
data.head(2)
print("Instances are: ", data[(data['Weather Condition'] == 'Clear') & (
    data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)])
print("\n")
