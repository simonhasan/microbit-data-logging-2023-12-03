# Import the pandas library
import pandas as pd # pandas for reading the CSV file and plotting

# Read the data from the CSV file
light_df = pd.read_csv('data/light.csv', # read the CSV file as a DataFrame
                       index_col=0) # index_col=0 to use the first column as the index

# Plot the data
light_plot = light_df.plot(title='Light Sensor Data') # plot all columns and add a title
