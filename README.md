# [Mean-Variance-Standard Deviation Calculator](https://github.com/borisTL/DataAnalyticsHub/tree/main/Mean-Variance-Standard%20Deviation%20Calculato)

This project implements a function called `calculate()` that takes a list of 9 numbers as input and returns various statistical metrics (mean, variance, standard deviation, max, min, and sum) for rows, columns, and the entire 3x3 matrix.

## Functionality
- The function accepts a list containing exactly 9 numbers.
- The input list is converted into a 3x3 NumPy array.
- The following statistical metrics are calculated:
  - Mean
  - Variance
  - Standard Deviation
  - Maximum
  - Minimum
  - Sum
- These metrics are calculated for:
  1. Each row
  2. Each column
  3. The entire matrix (flattened).
---
# [Demographic Data Analyzer](https://github.com/borisTL/DataAnalyticsHub/tree/main/Demographic%20Data%20Analyzer)

This project is a Python-based analysis tool that examines demographic data extracted from the 1994 Census database. It uses the Pandas library to perform various statistical analyses on the dataset, including calculations of average age, income distribution, and educational attainment.

 Project Features

- **Race Distribution**: Counts how many people of each race are represented in the dataset.
- **Average Age of Men**: Calculates the average age of male participants.
- **Education Analysis**: Calculates the percentage of people with a Bachelor's degree.
- **Income Analysis**: Determines what percentage of people with and without advanced education earn more than 50K.
- **Minimum Work Hours**: Identifies the minimum number of hours a person works per week.
- **Rich Percentage by Work Hours**: Calculates the percentage of people who work the fewest hours per week and earn more than 50K.
- **Highest-Earning Country**: Finds the country with the highest percentage of people earning more than 50K.
- **Popular Occupations in India**: Identifies the most popular occupation among those who earn more than 50K in India.
---
# [Medical Data Visualizer](https://github.com/borisTL/DataAnalyticsHub/tree/main/Medical%20Data%20Visualizer)

This project is designed to analyze and visualize medical examination data using Python, Pandas, and Seaborn. It performs data cleaning, generates categorical plots, and creates a heat map to help visualize the correlations between different health-related variables.

## Project Features

1. **Data Cleaning**:
   - Removes incorrect entries where diastolic pressure is higher than systolic pressure.
   - Filters out patients with extreme values for height and weight (below the 2.5th or above the 97.5th percentile).

2. **Overweight Column**:
   - A new column is added to indicate whether a patient is overweight based on their Body Mass Index (BMI). A BMI greater than 25 is classified as overweight.

3. **Normalization**:
   - The data for cholesterol and glucose levels are normalized so that 0 represents normal values and 1 represents above-normal values.

4. **Categorical Plot**:
   - Generates a categorical plot to display the distribution of several health indicators (cholesterol, glucose, smoking, alcohol consumption, activity level, and overweight) for patients with and without cardiovascular disease.

5. **Heat Map**:
   - Produces a heat map that shows the correlations between different features in the dataset, such as blood pressure, BMI, age, and cardiovascular disease.

---
# [Time Series Data Visualizer](https://github.com/borisTL/DataAnalyticsHub/tree/main/Page%20View%20Time%20Series%20Visualizer)

This project is a Python-based tool that analyzes and visualizes time series data using Pandas, Matplotlib, and Seaborn. The dataset represents daily page views of the freeCodeCamp Forum, and this tool helps visualize trends, monthly and yearly patterns, and the distribution of values over time.

## Project Features

1. **Data Cleaning**:
   - The dataset is cleaned by removing the top 2.5% and bottom 2.5% of the data to filter out anomalies and extreme values.

2. **Visualizations**:
   - **Line Plot**: Shows daily page views over time to visualize the overall trend.
   - **Bar Plot**: Displays the average page views for each month grouped by year.
   - **Box Plot**: Visualizes the distribution of page views over time, both yearly and monthly, to highlight trends and seasonality.

3. **Functions**:
   - `draw_line_plot()`: Generates a line plot showing daily page views.
   - `draw_bar_plot()`: Generates a bar plot showing monthly average page views.
   - `draw_box_plot()`: Generates box plots to visualize the distribution of data by year and by month.

---

