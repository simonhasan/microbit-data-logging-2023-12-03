# Import the accelerometer data and plot it
# Import the required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
accelerometer_df = pd.read_csv('data/accelerometer.csv', index_col=0)

# Plot the data with subplots
fig, axes = plt.subplots(nrows=3)

# Slice the data into x, y, and z columns
accelerometer_df['x'].plot(ax=axes[0])
accelerometer_df['y'].plot(ax=axes[1], color='red')
accelerometer_df['z'].plot(ax=axes[2], color='green')

# Add a title to the figure
fig.suptitle('Accelerometer Data')

# Display the plot
plt.show()
