# Weather Data Analysis 🌤️📊

This project performs an exploratory data analysis (EDA) on a year-long weather dataset. Using Python's pandas and matplotlib libraries, it answers key questions related to weather trends, statistical summaries, and visualizations.

---

## 📁 Dataset

The dataset used (`1. Weather Data.csv`) contains hourly weather data for one year with the following columns:

- `Date/Time`
- `Temp_C` (Temperature in °C)
- `Dew Point Temp_C`
- `Rel Hum_%` (Relative Humidity in %)
- `Wind Speed_km/h`
- `Visibility_km`
- `Press_kPa` (Pressure in kilopascals)
- `Weather` (Weather description)

---

## 📌 Key Objectives

1. **Handle missing values** — Identify and drop rows with null values.
2. **Analyze weather conditions** — Frequency of unique weather events.
3. **Rename columns** — Standardize column names for clarity.
4. **Filter data** — Based on specific conditions (e.g., clear weather, snow, wind speed, temperature).
5. **Compute statistics** — Mean, variance for weather metrics.
6. **Visualize data**:
   - Temperature variation over time using a line chart.
   - Weather condition distribution via pie chart.

---

## 🔧 Technologies Used

- **Python** 🐍
- **pandas** — For data cleaning and manipulation
- **matplotlib** — For visualization

---

## 📊 Sample Analysis

- Clear weather occurrences
- Snow-related temperature insights
- Variance of pressure readings
- Time-series graph of temperature
- Pie chart of frequent weather conditions

---

## 📷 Visuals

### Temperature Variation Over Time
Displays how the temperature changes hourly over a year.

### Weather Condition Pie Chart
Only includes conditions that occurred more than 20 times.

---

## ▶️ How to Run

1. Clone the repository:
   git clone https://github.com/AszadRaza3197/Weather-Data-Analysis.git
   cd Weather-Data-Analysis

2. Install dependencies (if not already):
pip install pandas matplotlib


3. Run the script:
python Weather-Data-Analysis.py
Make sure the CSV file 1. Weather Data.csv is in the same directory as the script.

🙋‍♂️ Author
Aszad Raza
📧 [raszad75@gmail.com]
🔗 [https://www.linkedin.com/in/aszad-raza/]
