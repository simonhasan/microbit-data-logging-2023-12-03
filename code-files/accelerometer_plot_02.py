# Import the accelerometer data and plot it
# Import the pandas library
import pandas as pd

# Read the data from the CSV file
accelerometer_df = pd.read_csv('data/accelerometer.csv', index_col=0)

# Plot the data
x_plot = accelerometer_df['x'].plot(title='Accelerometer Data (x)')