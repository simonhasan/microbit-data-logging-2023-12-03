# Imports go at the top
from microbit import *
import log
from octopus import Potentiometer

# Enable mirroring in serial
log.set_mirroring(True)

# Label the light column on the MY_DATA.HTM file
log.set_labels('analog_val')

# Create an instance of the Potentiometer class 
p = Potentiometer(pin1)

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed log the potentiometer data
    if button_a.is_pressed():
        # Add a row to MY_DATA.HTM
        log.add({
            'analog_val': p.get_analog()
        })
    # If button B is pressed delete MY_DATA.HTM    
    if button_b.is_pressed():
        # Delete MY_DATA.HTM
        log.delete()

    # Repeat every 10 milliseconds
    sleep(10)
