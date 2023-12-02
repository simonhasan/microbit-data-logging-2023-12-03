# Import the accelerometer data and plot it
# Import the required libraries
import pandas as pd # pandas for reading the CSV file
import matplotlib.pyplot as plt # matplotlib for plotting

# Read the data from the CSV file
accelerometer_df = pd.read_csv('data/accelerometer.csv', # Read the CSV file as a DataFrame
                               index_col=0) # Use the first column as the index

# Plot the data with subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, # 1 row of plots with 3 columns
                                    sharey=True) # sharey=True for a shared y-axis
ax1.plot(accelerometer_df['x']) # [x] in square brackets to slice the x column
ax1.set_title('x') # Add a title to the first plot
ax1.set_xlabel('Time (ms)') # Add a label to the x-axis

ax2.plot(accelerometer_df['y'], # [y] in square brackets to slice the y column
         color='red') # y in red
ax2.set_title('y') # Add a title to the second plot
ax2.set_xlabel('Time (ms)') # Add a label to the x-axis

ax3.plot(accelerometer_df['z'], # [z] in square brackets to slice the z column
         color='green') # z in green
ax3.set_title('z') # Add a title to the third plot
ax3.set_xlabel('Time (ms)') # Add a label to the x-axis

# Add a title to the figure
fig.suptitle('Accelerometer Data') # suptitle for the figure title

# Display the plot   
plt.show()
