# Imports go at the top
from microbit import *
import log
from octopus import Distance

# Delete MY_DATA.HTM if present
log.delete()

# Enable mirroring in serial
log.set_mirroring(True)

# Label the light column on the MY_DATA.HTM file
log.set_labels('distance')

# Create an instance of the Distance class 
dist = Distance(pin1)

# Code in a 'while True:' loop repeats forever
while True:
    # Add a row to MY_DATA.HTM 
    # This is returning an error
    # Argument does not match parameter type for parameter "data_dictionary"
    log.add({
        'distance': dist.get_distance()
    })
    
    # Repeat every 10 milliseconds
    sleep(10)
