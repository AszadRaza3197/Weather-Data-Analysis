import pandas as pd
import matplotlib.pyplot as plt

# Reading the csv file
df = pd.read_csv('1. Weather Data.csv')

# Shape of the data
print(df.shape)

# Q1: Check and drop null values
print(df.isnull().sum())
df.dropna(inplace=True)  # Drop rows with any NaNs

# Q2: Find unique instances of weather types
weather = df['Weather'].value_counts()
dfweather = pd.DataFrame(weather).reset_index()
dfweather.columns = ['Weather', 'Frequency']
print(dfweather)

# Q3: Rename 'Weather' column to 'Weather_Condition'
df.rename(columns={'Weather': 'Weather_Condition'}, inplace=True)

# Q4: Find all records when the weather was exactly clear
print(df[df['Weather_Condition'] == 'Clear'])

# Q5: Mean temperature, wind speed and visibility
print("Mean Temperature:", df['Temp_C'].mean())
print("Mean Wind Speed:", df['Wind Speed_km/h'].mean())
print("Mean Visibility:", df['Visibility_km'].mean())

# Q6: Variance of pressure
print("Pressure Variance:", df['Press_kPa'].var())

# Q7: Wind speed <= 30 km/h and temperature > 0 C
windspeed = df[(df['Wind Speed_km/h'] <= 30) & (df['Temp_C'] > 0)]
print(windspeed[['Date/Time', 'Wind Speed_km/h', 'Temp_C']])
print("Shape:", windspeed.shape)

# Q8: Date and temperature when snow was recorded
snow = df[df['Weather_Condition'] == 'Snow']
print(snow[['Date/Time', 'Temp_C']])

# Q9: Graph of temperature variation over time
graph = df[['Temp_C', 'Date/Time']]
graph.plot(x='Date/Time', y='Temp_C', figsize=(10, 7))
plt.title('Temperature Variation Over Time')
plt.xlabel('Date/Time')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Q10: Pie chart of weather conditions with frequency > 20
keep = dfweather[dfweather['Frequency'] > 20]
print(keep)
keep.set_index('Weather', inplace=True)
keep.plot.pie(y='Frequency', autopct='%1.1f%%', shadow=False, figsize=(12, 9))
plt.title("Weather Conditions")
plt.ylabel('')
plt.show()
