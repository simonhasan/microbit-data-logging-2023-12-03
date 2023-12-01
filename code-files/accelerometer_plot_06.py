# Import the accelerometer data and plot it
# Import the required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
accelerometer_df = pd.read_csv('data/accelerometer.csv', index_col=0)

# Plot the data with subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True) # 3 columns of plots with a shared y-axis
ax1.plot(accelerometer_df['x']) # x in blue (default) 
ax1.set_title('x') # Add a title to the first plot
ax1.set_xlabel('Time (ms)') # Add a label to the x-axis

ax2.plot(accelerometer_df['y'], color='red') # y in red
ax2.set_title('y') # Add a title to the second plot
ax2.set_xlabel('Time (ms)') # Add a label to the x-axis

ax3.plot(accelerometer_df['z'], color='green') # z in green
ax3.set_title('z') # Add a title to the third plot
ax3.set_xlabel('Time (ms)') # Add a label to the x-axis

# Add a title to the figure
fig.suptitle('Accelerometer Data')

# Display the plot   
plt.show()
