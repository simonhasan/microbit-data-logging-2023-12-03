# Import the accelerometer data and plot it
# Import the required libraries
import pandas as pd # pandas for reading the CSV file
import matplotlib.pyplot as plt # matplotlib for plotting

# Read the data from the CSV file
accelerometer_df = pd.read_csv('data/accelerometer.csv', # read the CSV file as a DataFrame
                               index_col=0) # index_col=0 to use the first column as the index

# Plot the data with subplots
# fig is the figure object
# ax1, ax2, and ax3 are the axes objects
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, # 3, 1 for 3 rows and 1 column of plots
                                    sharey=True) # sharey=True for a shared y-axis

# Plot the x, y, and z columns
# ax1 is the first axes object
ax1.plot(accelerometer_df['x'], # [x] in square brackets to slice the x column
         label='x') # Add a label to the first plot, x in blue (default)
ax1.set_title('x') # Add a title to the first plot

# ax2 is the second axes object
ax2.plot(accelerometer_df['y'], # [y] in square brackets to slice the y column
         label='y', # Add a label to the second plot
         color='red') # y in red
ax2.set_title('y') # Add a title to the second plot

# ax3 is the third axes object
ax3.plot(accelerometer_df['z'], # [z] in square brackets to slice the z column
         label='z', # Add a label to the third plot
         color='green') # z in green
ax3.set_title('z') # Add a title to the third plot

# Add a title to the figure
fig.suptitle('Accelerometer Data') # suptitle for the figure title
# Add a legend to the figure
fig.legend() 

# Display the plot
plt.show()