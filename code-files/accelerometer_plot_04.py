# Import the accelerometer data and plot it
# Importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
accelerometer_df = pd.read_csv('data/accelerometer.csv', index_col=0)

# Plot the data with subplots
fig, axes = plt.subplots(nrows=3) # 3 rows of plots


accelerometer_df['x'].plot(ax=axes[0]) # x in blue (default)
accelerometer_df['y'].plot(ax=axes[1], color='red') # y in red
accelerometer_df['z'].plot(ax=axes[2], color='green') # z in green

# Add a title to the figure
fig.suptitle('Accelerometer Data') 
# Add a legend to the figure
fig.legend()

# Display the plot
plt.show()
