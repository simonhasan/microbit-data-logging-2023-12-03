# Import the accelerometer data and plot it
# Import the required libraries
import pandas as pd # pandas for reading the CSV file
import matplotlib.pyplot as plt # matplotlib for plotting

# Read the data from the CSV file
accelerometer_df = pd.read_csv('data/accelerometer.csv', # read the CSV file as a DataFrame
                               index_col=0) # index_col=0 to use the first column as the index

# Plot the data with subplots
# fig is the figure object
# axes is an array of axes objects
fig, axes = plt.subplots(nrows=3) # nrows=3 for 3 rows of plots

# Slice the data into x, y, and z columns
accelerometer_df['x'].plot(ax=axes[0]) # x in blue (default)
accelerometer_df['y'].plot(ax=axes[1], color='red') # y in red
accelerometer_df['z'].plot(ax=axes[2], color='green') # z in green

# Add a title to the figure
fig.suptitle('Accelerometer Data')

# Display the plot
plt.show()
