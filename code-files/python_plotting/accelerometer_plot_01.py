# Import the accelerometer data and plot it
# Import the pandas library
import pandas as pd # pandas for reading the CSV file and plotting

# Read the data from the CSV file
accelerometer_df = pd.read_csv('data/accelerometer.csv', # read the CSV file as a DataFrame
                               index_col=0) # index_col=0 to use the first column as the index

# Plot the data
accelerometer_plot = accelerometer_df.plot(title='Accelerometer Data') # plot all columns and add a title