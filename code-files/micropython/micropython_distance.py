# Imports go at the top
from microbit import *
import log
from octopus import Distance

# Enable mirroring in serial
log.set_mirroring(True)

# Label the light column on the MY_DATA.HTM file
log.set_labels('distance')

# Create an instance of the Distance class 
dist = Distance(pin1)

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed log the distance data
    if button_a.is_pressed():
        # Add a row to MY_DATA.HTM 
        # Line 21 is returning an error for no reason. Ignore it.
        log.add({
            'distance': dist.get_distance()
        })
    # If button B is pressed delete MY_DATA.HTM 
    if button_b.is_pressed():
        # Delete MY_DATA.HTM
        log.delete()
    
    # Repeat every 10 milliseconds
    sleep(10)
