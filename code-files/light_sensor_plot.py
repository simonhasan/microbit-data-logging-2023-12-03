# Imort the pandas library
import pandas as pd

# Read the data from the CSV file
light_df = pd.read_csv('data/light.csv', index_col=0)

# Plot the data
light_plot = light_df.plot(title='Light Sensor Data')
